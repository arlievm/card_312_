from datetime import datetime


def get_upload_path(instance, filename):
    return os.path.join('categories/images/', datetime.now().date().strftime("%Y/%m/%d"), filename)


import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
