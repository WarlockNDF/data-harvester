from typing import Self

import io
from minio import Minio

from lib.config.minio_config import MinioConfig

class Storage:

    __bucket: str = ""
    __is_object_storage: bool = False
    __minio: Minio | None = None

    def __init__(self, bucket: str = ""):
        self.__bucket = bucket
        self.with_local("./storage/" + self.__bucket)

    def with_minio(self, config: MinioConfig) -> Self:
        self.__is_object_storage = True
        self.__minio = Minio(config.host, access_key=config.access_key, secret_key=config.secret_key)
        return self

    def with_local(self, path: str = "./storage/") -> Self:
        self.__is_object_storage = False
        return self

    def upload(self, file_name: str, data: bytes):
        if self.__is_object_storage:
            self.__minio_upload(file_name, data)
        else:
            self.__local_upload(file_name, data)

    def __minio_upload(self, file_name: str, data: bytes):
        self.__minio_bucket_prep()
        byte_stream = io.BytesIO(data)
        self.__minio.put_object(self.__bucket, file_name, byte_stream, length=len(data))

    def __minio_bucket_prep(self):
        exist = self.__minio.bucket_exists(self.__bucket)
        if not exist:
            self.__minio.make_bucket(self.__bucket)
            print("Creating Bucket : " + self.__bucket)
        else:
            print("Using Bucket : " + self.__bucket)

    def __local_upload(self, file_name: str, data: bytes):
        file_path = f"./${self.__bucket}/{file_name}"
        bytes_stream = io.BytesIO(data)
        with open(file_path, "wb") as f:
            f.write(bytes_stream.getbuffer())