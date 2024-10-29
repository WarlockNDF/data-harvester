from typing import Self

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
            pass
        else:
            pass

    def __minio__upload(self, file_name: str, data: bytes):
        pass