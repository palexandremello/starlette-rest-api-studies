from app.domain.entities.spreadsheet import Spreadsheet as SpreadsheetModel


def create_array_response(item):
    spreadsheet = SpreadsheetModel(id=item.id,
                            filename=item.filename,
                            initial_date=item.initial_date.strftime('%Y-%m-%d'),
                            final_date=item.final_date.strftime('%Y-%m-%d'),
<<<<<<< HEAD
                            link=item.link).to_dict()

=======
                            status=item.status.name,
                            link=item.link,
                            path=item.path).to_dict()
>>>>>>> 973ce23c1c917dfa6579b184c6b9f02c4acde0be
    return spreadsheet
