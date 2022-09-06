from types import List
from app.application.validation.validator import Validator
from io import BytesIO


class ValidatorBuilder:
    def __init__(self, value, field_name) -> None:
        self.value: any = value
        self.field_name: str = field_name
        self.validators: List[Validator] = []
    
    def of(self, value, field_name):
        super().__init__(value, field_name)
    

    def required(self):
        if isinstance(self.value, BytesIO):
            pass