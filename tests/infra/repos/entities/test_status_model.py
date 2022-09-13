from app.infra.repos.mysql.entities.status import Status


def test_should_be_repr_has_same_value_passed_on_constructor():
    sut = repr(Status(id=1, name='Novo'))
    assert sut == 'Status[name=(Novo)]'
