Extension = 'xlsx' or 'xls'

class AllowedMimeTypes:
    def __init__(self, mime_type) -> None:
        self.allowed =  Extension 
        self.mime_type: str = mime_type

    
    def validate(self) -> Exception | None:
        is_valid = False
        if (self.is_xlsx()):
            is_valid = True
        print(is_valid)
    
    def is_xlsx(self):
        return self.allowed.find('xlsx') and self.mime_type == 'application/vnd.ms-excel'