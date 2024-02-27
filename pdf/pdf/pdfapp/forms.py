from django import forms

from .models import uploadedPdf

class UploadPdfForm(forms.ModelForm):
    CHOICES = [
        ('file', 'Upload PDF File'),
        ('image', 'Upload image File')
    ]

    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)
    file = forms.FileField(required=False)
    image = forms.FileField(required=False)
    
    class Meta:
        model = uploadedPdf
        fields = ["file",'image']
        
    def clean(self):
        cleaned_data = super().clean()
        selected_choice = cleaned_data.get('choice_field')

        if selected_choice == 'file' and not cleaned_data.get('file'):
            self.add_error('file', 'Please upload a PDF file.')
        elif selected_choice == 'image' and not cleaned_data.get('image'):
            self.add_error('image', 'Please upload an image file.')

    # Add the selected_choice to the cleaned data
        cleaned_data['selected_choice'] = selected_choice

        return cleaned_data


    
