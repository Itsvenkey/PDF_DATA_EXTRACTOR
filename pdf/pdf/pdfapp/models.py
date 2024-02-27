from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


def fixed_filename(instance, filename):
    return 'pdf_files/sample.pdf'
def fixed_imagename(instance,filename):
    return 'image_files/sample.jpg'

class uploadedPdf(models.Model):
    file = models.FileField(upload_to=fixed_filename , validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='only PDF files are allowed. ')], help_text='upload a pdf file.')

    image = models.FileField(upload_to=fixed_imagename,validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'],message='only image files are allowed')],help_text='upload a image file')
    