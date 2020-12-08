import argparse
import dataclasses
import sys
import typing

from locusts import _builder
from locusts import _runner
from locusts import _starter


@dataclasses.dataclass(frozen=True)
class Context:
    """Data structure for command execution contexts."""

    args: typing.Dict[str, typing.Any]
    remainder: typing.List[str] = dataclasses.field(default_factory=lambda: [])


def _parse(arguments: typing.List[str] = None) -> "Context":
    """Parses the command line arguments."""
    source = arguments or sys.argv[1:]
    print("SOURCE:", source)
    parser = argparse.ArgumentParser(
        prog="locusts",
        description="Containerized Locust.io CI.",
    )
    parser.add_argument("command", choices=["run", "up", "build"])

    if "build" in source:
        _builder.populate(parser)
    elif "up" in source:
        _starter.populate(parser)
    elif "run" in source:
        print("POPULATING RUNNER...")
        _runner.populate(parser)

    parsed, remainder = parser.parse_known_intermixed_args(source)
    return Context(vars(parsed), remainder)


def main():
    """Execution entrypoint for locusts CLI invocations."""
    context = _parse()

    callables = {
        "build": _builder.run,
        "run": _runner.run,
        "up": _starter.run,
    }
    callables[context.args["command"]](context)
