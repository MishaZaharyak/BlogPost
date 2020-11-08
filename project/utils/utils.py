def get_file_upload_path(instance, filename):
    folder_name = f'{instance.__class__.__name__.lower()}'
    return f'{folder_name}/{filename}'
