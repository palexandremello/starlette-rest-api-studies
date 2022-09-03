
from app.application.errors.validation import RequiredFieldError
from app.application.validation.validator import Validator


class Required(Validator):
    def __init__(self, value: any, field_name: str) -> None:
        self.value = value
        self.field_name = field_name

    def validate(self) -> Exception or None:
        if (self.value == None or self.field_name == None):
            return RequiredFieldError(self.field_name)

