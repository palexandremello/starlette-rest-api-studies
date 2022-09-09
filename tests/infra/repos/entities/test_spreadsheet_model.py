from app.infra.repos.mysql.entities.spreasheet import Spreadsheet


def test_should_be_repr_has_same_value_passed_on_constructor():
    spreadsheet_data = {"id":'any_id', "filename":'any_file', "initial_date":'any_date', 'final_date':'any_date', "link":'any_link'}

    sut = repr(Spreadsheet(**spreadsheet_data))
    assert sut == 'Spreadsheet [filename=(any_file)]'
