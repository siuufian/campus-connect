from django.core.exceptions import ValidationError

def validate_nitc_email(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Only Gmail addresses are allowed.')

def validate(value1,value2):
    if not value2.endswith('_'+value1+'@nitc.ac.in'):
        raise ValidationError('Your username must be same as your roll no')