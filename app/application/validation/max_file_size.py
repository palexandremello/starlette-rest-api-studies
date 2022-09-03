
from app.application.errors.validation import MaxFileSizeError
from io import BytesIO

class MaxFileSize:
    def __init__(self, max_size_in_mb, buffer) -> None:
        self.max_size_in_mb : int = max_size_in_mb
        self.buffer: BytesIO = buffer

    def validate(self) -> Exception or None:
        max_file_size_in_bytes = self.max_size_in_mb * 1024 * 1024
        if (len(self.buffer.getvalue()) > max_file_size_in_bytes):
            return MaxFileSizeError(self.max_size_in_mb)