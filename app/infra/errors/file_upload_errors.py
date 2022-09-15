
class FileUploadErrors:
    
    @staticmethod
    def invalid_spreadsheet():
        return {"status_code": 500, "body": {"error": "Invalid spreadsheet file"}}
