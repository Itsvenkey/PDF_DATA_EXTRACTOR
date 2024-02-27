from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import UploadPdfForm
from django.conf import settings
from .models import uploadedPdf

# Create your views here.


import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import re

def convert_pdf_to_images(pdf_path, output_folder=r'media\output_images'):
    
    output_folder_path = os.path.join(settings.BASE_DIR, 'pdfapp', output_folder)
    os.makedirs(output_folder_path, exist_ok=True)
    images = convert_from_path(pdf_path, output_folder=output_folder, fmt='png')
    image_path = os.path.join(output_folder, 'image.png')
    
    # Save only the first image as 'image.png'
    images[0].save(image_path, 'PNG')

    # Remove other image files in the output folder
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        if filename != 'image.png' and os.path.isfile(file_path):
            os.remove(file_path)

    return images

def image_to_text(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    
    pattern = r'(\b\w+(\s\w+)*\b):\s?([^,\n]+)'
    text = pytesseract.image_to_string(Image.open(image_path))
    
    # Find all matches in the input string
    matches = re.findall(pattern, text)

    # Create a dictionary from the matches
    result = {}

    # Process each match
    result = {key.strip(): value.strip() for key, _, value in matches}
    return result

def pdf_to_text(uploaded_pdf):
    # Get the PDF file from the UploadedPdf instance
    pdf_file = uploaded_pdf.file

    # Construct the file path for image output (modify as needed)
    output_folder = f'{settings.BASE_DIR}\pdfapp\media\output_images'
    output_file_path = os.path.join(output_folder, 'image.png')

    # Convert the PDF to images and save them
    convert_pdf_to_images(pdf_file.path, output_folder)

    # Perform OCR on the saved image and get text
    text = image_to_text(os.path.join(settings.BASE_DIR, 'pdfapp', output_folder, 'image.png'))

    return text


def home(request):
    if request.method == 'POST':
        form = UploadPdfForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save()
             
            user_choice = form.cleaned_data.get('selected_choice')
            if user_choice == 'file':
                text = pdf_to_text(instance)
                
                instance.file.delete()
                instance.delete()
                return render(request,'pdfapp/response.html',{'text':text})
            
            elif user_choice == 'image':
                text = image_to_text(instance.image.path)
                instance.image.delete()
                instance.delete()
                return render(request,'pdfapp/response.html',{'text':text})

                
                
    else:
        form = UploadPdfForm()
            
    return render(request,'pdfapp/index.html',{'form':form})