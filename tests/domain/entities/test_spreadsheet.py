from app.domain.entities.spreadsheet import Spreadsheet
def test_should_be_able_create_a_Spreadsheet_object():
    conciliation = {"id":'any_id', "filename":'any_file', "initial_date":'any_date', 'final_date':'any_date', "link":'any_link'}
    sut = Spreadsheet(**conciliation)

    assert sut.filename == conciliation['filename']
    assert sut.initial_date == conciliation['initial_date']
    assert sut.final_date == conciliation['final_date']
    assert sut.link == conciliation['link']
    assert sut.id == conciliation['id']
