from django.core.exceptions import ValidationError


def validate_file_size(value):

    if value.size > 1048576:
        raise ValidationError("You cannot upload an image larger than 1 MB")
    else:
        return value
