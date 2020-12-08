import argparse
import json
import pathlib
import subprocess
import sys
import typing

from locusts import _cli


def populate(parser: argparse.ArgumentParser):
    """Populates the run command CLI arguments."""
    parser.add_argument(
        "--main-host",
        dest="main_host",
        default=None,
        help="The hostname/ip of the main instance",
    )


def get_locust_file() -> typing.Optional[pathlib.Path]:
    """Finds the path to the locust file located in the scripts directory."""
    names = ["locustfile.py", "locust_file.py", "locust.py"]
    directory = pathlib.Path("/scripts")
    return next((path for n in names if (path := directory.joinpath(n)).exists()), None)


def make_command(args: dict) -> typing.List[str]:
    """Creates the command that executes the locust process in the container."""
    command = [
        "locust",
        "-f",
        '"{}"'.format(get_locust_file()),
        "--master" if args["is_main"] else "--worker",
        "--host={}".format(args["target"]),
    ]

    if not args.get("is_main"):
        command.append("--master-host={}".format(args["main_host"]))

    try:
        users = args["users"]
        command += [users] if hasattr(users, "find") else users
    except Exception:
        print('[ERROR]: Invalid or missing "users" config attribute')
        raise

    return command


def run(context: "_cli.Context"):
    """Entrypoint for the locust image."""
    args = json.loads(pathlib.Path("/scripts/locust.config.json").read_text())
    args.update(context.args)
    args["is_main"] = args["main_host"] is None

    command = make_command(args)
    print(" ".join(command).replace(" -", "\n   -"))
    process = subprocess.Popen(
        args=" ".join(command),
        stdout=sys.stdout,
        shell=True,
        universal_newlines=True,
    )
    process.wait()
