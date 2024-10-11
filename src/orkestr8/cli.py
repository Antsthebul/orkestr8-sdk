from argparse import ArgumentParser


def parse_args():
    base_parser = ArgumentParser(add_help=False)
    base_parser.add_argument("--aws-access-key", nargs="?", action="store")
    base_parser.add_argument("--aws-secret-key", nargs="?", action="store")
    base_parser.add_argument("--aws-bucket-name", nargs="?", action="store")
    base_parser.add_argument("--project-location", nargs="?", action="store")
    base_parser.add_argument(
        "-y",
        dest="default_yes",
        action="store_true",
        help="Apply yes by default to all inputs",
    )

    # This creates 'mutually' exclusive parsers
    parser = ArgumentParser(prog="Orchkestr8 ML train runner")
    subparsers = parser.add_subparsers(dest="command", help="Invocation commands")
    # This creates 'mutually' exclusive parsers

    train_parser = subparsers.add_parser(
        "train", help="Runs the training logic only", parents=[base_parser]
    )
    train_parser.add_argument(
        "model_module",
        action="store",
        help="The module that contains the model to run. Module MUST have a `run` method defined",
    )

    run_parser = subparsers.add_parser(
        "run", help="Runs the data update and training logic", parents=[base_parser]
    )
    run_parser.add_argument(
        "--model-module",
        action="store",
        help="The module that contains the model to run. Module MUST have a `run` method defined",
    )
    run_parser.add_argument(
        "--remote_file_path", help="Where to direct Orkestr8 to pull the file from"
    )
    run_parser.add_argument(
        "--dest_file_path", help="Where to direct Orkestr8 to write file path"
    )

    update_parser = subparsers.add_parser(
        "update", help="Runs the data update function.", parents=[base_parser]
    )
    update_parser.add_argument(
        "remote_file_path", help="Where to direct Orkestr8 to pull the file from"
    )
    update_parser.add_argument(
        "dest_file_path", help="Where to direct Orkestr8 to write file path"
    )

    # ArgumentParser("stop", description="Writes to a file", parents=[parser])
    return parser.parse_args()
