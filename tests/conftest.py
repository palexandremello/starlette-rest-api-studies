import sys
import pytest
import os
import csv, io
from sqlalchemy_utils import drop_database
from app.infra.repos.config import DatabaseConnectionHandler, Base
from starlette.requests import Request
from starlette.datastructures import Headers
from starlette.datastructures import UploadFile

sys.path[0] = "app"

@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    os.environ['DATABASE_STRING_URL'] = "sqlite:///storage.db"
    database_handler = DatabaseConnectionHandler()
    engine = database_handler.get_engine()
    Base.metadata.create_all(engine)
    yield                            # Run the tests.



@pytest.fixture(scope="session", autouse=True)
def invalid_buffer():
    test_data = [[1, 2, 3], [1, 2, 3]]
    s = io.StringIO()
    csv.writer(s).writerows(test_data)
    s.seek(0)
    buf = io.BytesIO()
    buf.write(s.getvalue().encode())
    buf.seek(0)
    return buf

@pytest.fixture(scope="session", autouse=True)
def valid_buffer():
    os.environ["PORTAL_TRANSPORTADORA_BUCKET"] = "portal-transportadora-bucket"
    os.environ["LOCALSTACK_URL"] = "http://localhost:4566"
    bytesObject = b'\x65\x66\x67\x00\x10\x00\x00\x00\x04\x00'
    return bytesObject

@pytest.fixture(scope="session", autouse=True)
def valid_uploadFile():
    return UploadFile('any_filename.xlsx', io.BytesIO(), content_type="xlsx")

@pytest.fixture(scope="session", autouse=True)
def s3_response():
    put_object_response = {   'ETag': '"14fe4f49fffffffffff9afbaaaaaaaa9"',
    'ResponseMetadata': {   'HTTPHeaders': {   'content-length': '0',
                                               'date': 'Wed, 08 Apr 2020 '
                                                       '20:35:42 GMT',
                                               'etag': '"14fe4f49fffffffffff9afbaaaaaaaa9"',
                                               'server': 'AmazonS3',
                                               },
                            'HTTPStatusCode': 200,
                            'HostId': 'GEHrJmjk76Ug/clCVUwimbmIjTTb2S4kU0lLg3Ylj8GKrAIsv5+S7AFb2cRkCLd+mpptmxfubLM=',
                            'RequestId': 'A8FFFFFFF84C3A77',
                            'RetryAttempts': 0},
    'VersionId': 'Dbc0gbLVEN4N5F4oz7Hhek0Xd82Mdgyo'}
    return put_object_response

@pytest.fixture(scope="session", autouse=True)
def build_request(
    method: str = "GET",
    server: str = "www.example.com",
    path: str = "/",
    headers: dict = None,
    body: str = None,
    form: str = None,
) -> Request:
    if headers is None:
        headers = {}
    request = Request(
        {
            "type": "http",
            "path": path,
            "headers": Headers(headers).raw,
            "http_version": "1.1",
            "method": method,
            "scheme": "https",
            "client": ("127.0.0.1", 8080),
            "server": (server, 443),
        }
    )
    if body:

        async def request_body():
            return body

        request.body = request_body
    
    if form:
        async def request_form():
            return form
        request.form = request_form
    return request
