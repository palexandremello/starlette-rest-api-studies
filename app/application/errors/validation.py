class RequiredFieldError(Exception):
    def __init__(self, field_name: str):
        self.message = 'Field required' if field_name == None else f'The field {field_name} is required'
        print(self.message)
        super().__init__(self.message)


class MaxFileSizeError(Exception):
    def __init__(self, max_size_in_mb) -> None:
        self.message = f'File upload limit is {max_size_in_mb} MB'
        super().__init__(self.message)

class InvalidMimeTypeError(Exception):
    def __init__(self, allowed: str) -> None:
        self.message = f'Unsupported file. Allowed extensions {allowed}'
        super().__init__(self.message)