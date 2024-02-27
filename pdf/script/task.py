# import os
# from pdf2image import convert_from_path
# from PIL import Image
# import pytesseract
# import re
# import csv

# def convert_pdf_to_images(pdf_path, output_folder='assests/images/'):
#     os.makedirs(output_folder,exist_ok=True)
#     images = convert_from_path(pdf_path, output_folder=output_folder, fmt='png')
#     image_path = os.path.join(output_folder, 'image.png')
    
#     # Save only the first image as 'image.png'
#     images[0].save(image_path, 'PNG')

#     # Remove other image files in the output folder
#     for filename in os.listdir(output_folder):
#         file_path = os.path.join(output_folder, filename)
#         if filename != 'image.png' and os.path.isfile(file_path):
#             os.remove(file_path)

#     return images,image_path



# def image_to_csv(image_path,csv_output):
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#     os.makedirs(image_path,exist_ok=True)
#     pattern = r'(\b\w+(\s\w+)*\b):\s?([^,\n]+)'
#     text = pytesseract.image_to_string(Image.open(image_path))
    
#     # Find all matches in the input string
#     matches = re.findall(pattern, text)

#     # Prepare data for CSV
#     data = [(key.strip(), value.strip()) for key, _, value in matches]

#     # Save data to CSV
#     with open(csv_output, mode='w', newline='') as csvfile:
#         fieldnames = ['Key', 'Value']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()
#         for key, value in data:
#             writer.writerow({'Key': key, 'Value': value})

#     print(f"Data saved to {'output.csv'}")
    
    
# def pdf_to_csv(pdf_path):
#     # Get the PDF file from the UploadedPdf instance
    

#     # Construct the file path for image output (modify as needed)
#     output_folder = 'csv_files/'
#     output_file_path = os.path.join(output_folder, 'image.png')
#     csv_ouput = output_folder

#     # Convert the PDF to images and save them
#     convert_pdf_to_images(pdf_path, output_folder)

#     # Perform OCR on the saved image and get text
#     image_to_csv(output_file_path,output_folder)

#     return 



# print(pdf_to_csv('sample4.pdf'))

import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import re
import csv

def convert_pdf_to_images(pdf_path, output_folder='assets/images/'):
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path, output_folder=output_folder, fmt='png')
    image_path = os.path.join(output_folder, 'image.png')

    # Save only the first image as 'image.png'
    images[0].save(image_path, 'PNG')

    # Remove other image files in the output folder
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        if filename != 'image.png' and os.path.isfile(file_path):
            os.remove(file_path)

    return image_path

def image_to_csv(image_path, name = 'image_output.csv'):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    
    pattern = r'(\b\w+(\s\w+)*\b):\s?([^,\n]+)'
    text = pytesseract.image_to_string(Image.open(image_path))
    
    # Find all matches in the input string
    matches = re.findall(pattern, text)

    # Prepare data for CSV
    data = [(key.strip(), value.strip()) for key, _, value in matches]
    output_folder = 'csv_files/'
    path = os.path.join(output_folder, name)
    
    # Save data to CSV
    with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Key', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for key, value in data:
            writer.writerow({'Key': key, 'Value': value})
            
    for filename in os.listdir('csv_files/'):
        file_path = os.path.join('csv_files/', filename)
        if filename == 'image.png' and os.path.isfile(file_path):
            os.remove(file_path)
    print(f"Data saved to ")

def pdf_to_csv(pdf_path):
    # Construct the file path for image output (modify as needed)
    output_folder = 'csv_files/'
    name = 'pdf_output.csv'

    # Convert the PDF to images and save them
    image_path = convert_pdf_to_images(pdf_path, output_folder)

    # Perform OCR on the saved image and save text to CSV
    image_to_csv(image_path, name)

    return


# to extract data from pdf

print(pdf_to_csv('sample2.pdf'))


# to extract data from image

print(image_to_csv('sample4.jpg'))