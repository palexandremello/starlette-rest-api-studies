from app.main.adapter.starlette_adapter import starlette_adapter

from app.main.composite.list_spreadsheet_composite import list_spreadsheet_composer
from starlette.responses import JSONResponse

async def list_spreadsheet(request):

    message = {}
    response = await starlette_adapter(request=request, api_route=list_spreadsheet_composer())
    
    if response.status_code < 300:
        message = {
            "type": "spreadsheet",
            "body": response.body
        }
        return JSONResponse(message, status_code=response.status_code)
    return  JSONResponse({"error": {"status": response.status_code, "title": response.body["error"]}}, status_code=response.status_code)
    