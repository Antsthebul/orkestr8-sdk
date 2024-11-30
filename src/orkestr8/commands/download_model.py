import os
from dataclasses import dataclass
from enum import Enum

from orkestr8.clients.data_lake_client import ClientType, DataLakeClient

from .base import Command


class Destination(Enum):
    LOCAL = "LOCAL"
    S3 = "S3"


@dataclass
class DownloadModelArgs:
    source: str
    destination: str
    to: Destination


class DownloadModelCommand(Command[DownloadModelArgs]):
    @staticmethod
    def parse(args) -> DownloadModelArgs:
        return DownloadModelArgs(
            source=args.source, to=args.to, destination=args.destination
        )

    def run(self):
        AWS_BUCKET_NAME = os.environ["AWS_BUCKET_NAME"]
        if self.args.to == Destination.S3:
            cl = DataLakeClient(ClientType.S3, AWS_BUCKET_NAME)

            with open(self.args.source, "rb") as d:
                cl.put_object(self.args.destination, d)