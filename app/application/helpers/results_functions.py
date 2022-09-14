from app.domain.entities.spreadsheet import Spreadsheet as SpreadsheetModel


def create_array_response(item):
    spreadsheet = SpreadsheetModel(id=item.id,
                            filename=item.filename,
                            initial_date=item.initial_date.strftime('%Y-%m-%d'),
                            final_date=item.final_date.strftime('%Y-%m-%d'),
                            link=item.link,
                            status = item.status.name,
                            created_at = item.created_at.strftime('%Y-%m-%d'),
                            updated_at = item.updated_at.strftime('%Y-%m-%d'),
                            path = item.path,
                            status_id= item.status_id
                            ).to_dict()
    return spreadsheet
