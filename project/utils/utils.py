from rest_framework.settings import api_settings


def create_error(message, extra=False, field_name=api_settings.NON_FIELD_ERRORS_KEY):
    """
    param: message - error message
    param: extra - an object with extra key value pairs
    param: field_name - str, error field name
    return: error response object
    """
    message = message if isinstance(message, list) else [str(message)]

    if not extra:
        return {'errors': {field_name: message}}

    extra = extra if isinstance(extra, dict) else {}
    return {**extra, 'errors': {field_name: message}}


def get_file_upload_path(instance, filename):
    folder_name = f'{instance.__class__.__name__.lower()}'
    return f'{folder_name}/{filename}'