from app.domain.entities.spreadsheet import Spreadsheet as SpreadsheetModel


def create_array_response(item):
    spreadsheet = SpreadsheetModel(id=item.id,
                            filename=item.filename,
                            initial_date=item.initial_date.strftime('%Y-%m-%d'),
                            final_date=item.final_date.strftime('%Y-%m-%d'),
                            status=item.status.name,
                            link=item.link).to_dict()
    return spreadsheet
