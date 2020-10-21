import os

from django.core.exceptions import ValidationError


def validate_pdf_extension(value):
    ext = os.path.splitext(value.name)[1]
    # valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Загружать можно только PDF.')