
class HttpErrors:
    
    @staticmethod
    def error_422():
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}
    
    @staticmethod
    def error_400():
        return {"status_code": 400, "body": {"error": "Bad Request"}}
    
    @staticmethod
    def error_409():
        return {"status_code": 409, "body": {"error": "Conflict"}}
    

    @staticmethod
    def error_500():
        return {"status_code": 500, "body": {"error": "Internal Server Error"}}
