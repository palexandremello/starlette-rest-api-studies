from app.domain.entities.spreadsheet import Spreadsheet
def test_should_be_able_create_a_Spreadsheet_object():
    spreadsheet_data = {"id":'any_id', "filename":'any_file', "initial_date":'any_date', 'final_date':'any_date', "link":'any_link'}

    sut = Spreadsheet.from_dict(spreadsheet_data)

    assert sut.to_dict() == spreadsheet_data