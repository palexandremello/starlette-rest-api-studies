from io import BytesIO
from app.domain.entities.file import File

def test_should_be_able_create_a_File_model_object():
    file_spreadsheet = {"filename":'any_filename', "size": 100, "type":'any_type', 'extension':'any_extension', "content": bytes('any_content', 'utf-8')}

    sut = File.from_dict(file_spreadsheet)

    assert sut.to_dict() == file_spreadsheet
