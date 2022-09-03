class RequiredFieldError(Exception):
    def __init__(self, field_name: str):
        self.message = 'Field required' if field_name == None else f'The field {field_name} is required'
        print(self.message)
        super().__init__(self.message)