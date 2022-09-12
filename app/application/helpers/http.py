
from typing import Dict


class HttpRequest:
    def __init__(self, header: Dict = None, body: Dict = None, form: Dict = None, query: Dict = None):
        self.header = header
        self.body = body
        self.form = form
        self.query = query

    
    def __repr__(self) -> str:
        return (
            f"HttpRequest (header={self.header}, body={self.body}, form={self.form} query={self.query})"
        )


class HttpResponse:
    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body
    
    def __repr__(self) -> str:
        return (
            f"HttpResponse (status_code={self.status_code}, body={self.body})"
        )