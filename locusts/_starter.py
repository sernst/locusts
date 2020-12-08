import argparse
import pathlib
import subprocess

from locusts import _cli


def populate(parser: argparse.ArgumentParser):
    """Populate the command args for the start/up command."""
    parser.add_argument(
        "-d",
        "--directory",
        default=str(pathlib.Path().absolute()),
        help="Directory containing the locusts scripts to execute.",
    )
    parser.add_argument(
        "--main-host",
        dest="main_host",
        default=None,
        help="The hostname/ip of the main instance",
    )


def run(context: "_cli.Context"):
    """
    Executes the up command, starting the locusts container in the specified directory.
    """
    scripts_directory = pathlib.Path(context.args["directory"]).absolute()
    main_host = context.args.get("main_host")

    command = [
        "docker",
        "run",
        "-it",
        "--rm",
        "-v",
        "{}:/scripts".format(scripts_directory),
    ]

    if main_host is None:
        command += ["-p", "8089:8089", "-p", "5557:5557"]

    command.append("swernst/locusts")

    if main_host:
        command.append(f"--main-host={main_host}")

    command += context.remainder or []

    print(" ".join(command).replace(" -", "\n   -"))
    subprocess.run(command)
