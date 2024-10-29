from typing import Self

class Storage:

    bucket: str = ""
    is_object_storage: bool = False

    def __init__(self, bucket: str = ""):
        self.bucket = bucket
        self.with_local("./storage/" + self.bucket)

    def with_minio(self) -> Self:
        self.is_object_storage = True
        return self

    def with_local(self, path: str = "./storage/") -> Self:
        self.is_object_storage = False
        return self

    def upload(self, file_name: str, data: bytes):
        if self.is_object_storage:
            pass
        else:
            pass