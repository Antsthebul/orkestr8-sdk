import os
from uuid import uuid4

from orkestr8.clients.data_lake_client import DataLakeClient

from .base import Command


class UpdateCommand(Command):
    @staticmethod
    def __rename_dir(old, new_=None):
        new_name = new_
        if new_ is None:
            new_name = str(uuid4())
        try:
            os.rename(old, new_name)
            return new_name
        except Exception as e:
            raise Exception(f"Renaming file failed. {str(e)}")

    @classmethod
    def run(cls, args):
        """Pulls down data from repo"""
        AWS_BUCKET_NAME = os.environ["AWS_BUCKET_NAME"]

        remote_path, dest_path = (
            args.update.remote_file_path,
            args.update.dest_file_path,
        )

        cl = DataLakeClient("s3", AWS_BUCKET_NAME)
        if not args.default_yes:
            confirm = input(
                "Update is a desctructive operation. The path will be completely overwritten ['Enter y to continue']. "
            )
            if confirm != "y":
                print("Exiting..")
                return

        new_name = cls.__rename_dir(dest_path)

        try:
            cl.get_object(remote_path, new_name)
        except Exception as e:
            cls.__rename_dir(new_name, dest_path)
            print(f"Failed to perform update operation. {type(e).__name__}:{str(e)}")
        finally:
            os.removedirs(new_name)
            print("Successfully updated")
