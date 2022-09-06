
from app.application.errors.validation import RequiredFieldError
from app.application.validation.validator import Validator


class Required(Validator):
    def __init__(self, value: any, field_name: str) -> None:
        self.value = value
        self.field_name = field_name

    def validate(self) -> Exception or None:
        if (self.value == None or self.field_name == ''):
            return RequiredFieldError(self.field_name)

class RequiredString(Required):
    def __init__(self, value: any, field_name: str) -> None:
        super().__init__(value, field_name)

    def validate(self) -> Exception or None:
        if (super().validate() != None or self.value == ''):
            return RequiredFieldError(self.field_name)

class RequiredBuffer(Required):
    def __init__(self, value: any, field_name: str = None) -> None:
        super().__init__(value, field_name)
    
    def validate(self) -> Exception or None:
        print(self.value)
        if(super().validate() != None or len(self.value.getvalue()) == 0):
            return RequiredFieldError(self.field_name)

class RequiredSpreadsheetIntegration(Required):
    def __init__(self, value: any, field_name: str = None) -> None:
        super().__init__(value, field_name)
    
    def validate(self) -> Exception or None:
        if(super().validate() != None or self.value == ''):
            return RequiredFieldError(self.field_name)
