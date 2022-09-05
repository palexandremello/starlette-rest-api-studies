from typing import List

from app.application.errors.validation import InvalidMimeTypeError


class AllowedMimeTypes:
    def __init__(self, allowed_type, mime_type) -> None:
        self.allowed: List =  allowed_type 
        self.mime_type: str = mime_type
    
    def validate(self) -> Exception or None:
        is_valid = False
        if (self.is_xlsx()):
            print("entrou aqui xlsx")
            is_valid = True
        elif (self.is_xls()):
            print("entrou aqui xls")
            is_valid = True
        
        if not is_valid: return InvalidMimeTypeError(self.allowed)
    
    def is_xlsx(self):
        return 'xlsx' in self.allowed and self.mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    
    def is_xls(self):
        return 'xls' in self.allowed and self.mime_type == 'application/vnd.ms-excel'