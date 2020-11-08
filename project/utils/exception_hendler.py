from rest_framework.views import exception_handler
from rest_framework.settings import api_settings


def custom_exception_handler(exc, context):
    """
    custom exception handler
    returns your custom error response
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None:
        try:
            errors = {api_settings.NON_FIELD_ERRORS_KEY: [response.data['detail']]}
        except (KeyError, TypeError):
            errors = response.data
        response.data = dict()
        response.data['errors'] = errors
    return response
