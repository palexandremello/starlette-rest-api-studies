import pytest
from unittest.mock import AsyncMock
from app.application.controllers.controller import Controller
from app.application.errors.http import ServerError
from app.application.helpers.http import HttpResponse

class ControllerStub(Controller):
    result: HttpResponse = {
        "status_code": 200,
        "data": 'any_data'
    }
    
    async def perfom(self, http_request: any) -> HttpResponse:
        return self.result


@pytest.fixture()
def mock_perfom(mocker):
    async_mock = AsyncMock()
    mocker.patch('tests.application.controllers.test_controller.ControllerStub.perfom', side_effect=async_mock)
    return async_mock

@pytest.mark.asyncio
async def test_should_return_same_result_as_perfom():
    sut = ControllerStub()
    http_response = await sut.handle('any_value')
    assert http_response == sut.result

@pytest.mark.asyncio
async def test_should_return_500_if_perfom_throws(mock_perfom):
    sut = ControllerStub()
    error = Exception
    mock_perfom.side_effect= error
    with pytest.raises(error):
        http_response = await sut.handle('any_value')
        assert http_response == {
            'status_code': 500,
            'data': ServerError(),
        }