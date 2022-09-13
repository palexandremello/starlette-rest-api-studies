from app.infra.repos.mysql.entities.status import Status


def test_should_be_repr_has_same_value_passed_on_constructor():
    spreadsheet_data = {"id":'any_id', "filename":'any_file', "initial_date":'any_date', 'final_date':'any_date', "link":'any_link'}

    sut = repr(Status(id=1, name='Novo'))
    assert sut == 'Status[name=(Novo)]'
