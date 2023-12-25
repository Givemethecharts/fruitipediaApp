from django.core.exceptions import ValidationError


def fruit_name_only_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Fruit name should contain only letters!')

