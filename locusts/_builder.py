import argparse
import pathlib
import subprocess

from locusts import _cli


def _get_locust_version():
    """Attempt to retrieve the version of locust being installed."""
    commands = [
        ("locust", "--version"),
        ("poetry", "run", "locust", "--version"),
    ]

    for command in commands:
        response = subprocess.run(list(command), stdout=subprocess.PIPE)
        if response.returncode == 0:
            return response.stdout.decode().strip().rsplit(" ", 1)[-1]

    raise RuntimeError("Unable to determin locust version.")


def populate(parser: argparse.ArgumentParser):
    """Populates the run command CLI arguments."""
    parser.add_argument("--push", action="store_true")


def run(context: "_cli.Context"):
    """Executes a build (and push) of the locusts image to dockerhub."""
    tags = [
        "swernst/locusts:latest",
        "swernst/locusts:{}".format(_get_locust_version()),
    ]

    command = ["docker", "build"]

    for tag in tags:
        command += ["-t", tag]

    command.append(str(pathlib.Path()))

    print("[building] Locusts container image...")
    subprocess.run(command)
    print("[complete] Image build process has completed.")

    if not context.args.get("push"):
        return

    print("[pushing] Publishing images to dockerhub...")
    for tag in tags:
        subprocess.run(["docker", "push", tag])
        print(f"[pushed] {tag}")
