import os
from app.infra.gateways.aws_s3_file_upload import AwsS3FileUpload
from app.data.repositories.upload_spreadsheet import UploadSpreadsheet
from app.application.services.file_upload_service import FileUploadService


def file_upload_service_composer():
    """ Composing File Upload Service
    :param - None
    :return - Object with File Upload Service
    """
    print(os.environ.get('PORTAL_TRANSPORTADORA_BUCKET'))
    file_uploader = AwsS3FileUpload(bucket=os.environ.get('PORTAL_TRANSPORTADORA_BUCKET'))
    use_case = UploadSpreadsheet(file_uploader)
    upload_file_service = FileUploadService(use_case)

    return upload_file_service