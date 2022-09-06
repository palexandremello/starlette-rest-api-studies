from app.application.validation.validator import Validator

class ValidationComposite(Validator):
    def __init__(self, validators) -> None:
        self.validators: Validator = validators

    def validate(self) -> Exception or None:
        for validator in self.validators:
            error = validator.validate()
            if error != None:
                return error
