from app.domain.entities.spreadsheet import Spreadsheet as SpreadsheetModel


def create_array_response(item):
    spreadsheet = SpreadsheetModel(id=item.id,
                            filename=item.filename,
                            initial_date=item.initial_date.strftime('%Y-%m-%d'),
                            final_date=item.final_date.strftime('%Y-%m-%d'),
                            link=item.link).to_dict()
    # spreadsheet['initial_date'] = spreadsheet['initial_date'].strftime('%Y-%m-%d')
    # spreadsheet['final_date'] = spreadsheet['final_date'].strftime('%Y-%m-%d')

    return spreadsheet
