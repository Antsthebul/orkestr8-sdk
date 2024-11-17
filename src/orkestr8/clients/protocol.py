from datetime import datetime
from typing import BinaryIO, Generator, Protocol, TypedDict


class Result(TypedDict):
    Key: str
    LastModified: datetime


class DatalakeProtocol(Protocol):
    def download_object(
        self, bucket_name: str, obj_name: str, dest_file_path: str
    ) -> None:
        ...

    def download_object_as_file(self, bucket_name: str, obj_name: str) -> BinaryIO:
        ...

    def list_objects(
        self, bucket_name: str, prefix: str
    ) -> Generator[Result, None, list]:
        ...

    def put_object(self, bucket_name: str, path: str, data: BinaryIO) -> None:
        ...
