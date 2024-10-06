import os
from uuid import uuid4

from orkestr8.clients.data_lake_client import DataLakeClient


def run(args):
    """Pulls down data from repo"""
    AWS_BUCKET_NAME = os.environ["AWS_BUCKET_NAME"]

    remote_path, dest_path = args.update.remote_file_path, args.update.dest_file_path

    cl = DataLakeClient("s3", AWS_BUCKET_NAME)
    if not args.default_yes:
        confirm = input(
            "Update is a desctructive operation. The path will be completely overwritten ['Enter y to continue']. "
        )
        if confirm != "y":
            print("Exiting..")
            return

    name = uuid4()
    try:
        os.rename(dest_path, name)
        cl.get_object(remote_path, dest_path)
    except Exception as e:
        print(f"Failed to perform update operatoin due to {type(e)}:{str(e)}")
    finally:
        os.removedirs(dest_path)
    print("Successfully updated")
