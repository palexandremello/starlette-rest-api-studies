from app.main.adapter.starlette_adapter import starlette_adapter

from app.main.composite.create_spreadsheet_composite import create_spreadsheet_composer
from starlette.responses import JSONResponse

async def create_spreadsheet(request):
    message = {}
    response = await starlette_adapter(request=request, api_route=create_spreadsheet_composer())
    if response.status_code < 300:
        message = {
            "type": "spreadsheet",
            "attributest": {"filename": response.body.filename,
                            "initial_date": response.body.initial_date,
                            "final_date": response.body.final_date}
        }

        return JSONResponse({"data": message})

    return  JSONResponse({"error": {"status": response.status_code, "title": response.body["error"]}}, status_code=response.status_code)
    