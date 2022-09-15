import sys
import pytest
import os
import csv, io
from sqlalchemy_utils import drop_database
from app.infra.repos.config import DatabaseConnectionHandler, Base

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
    data = b'Hello World\n'
    fh = io.BytesIO()
    fh.write(data)
    fh.seek(0)
    return fh


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