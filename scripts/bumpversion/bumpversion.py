import re
from typing import Dict

import rich_click as click
import versioningit

_SEMVER = re.compile(
    r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"  # noqa, pylint: disable=line-too-long
)


@click.command("bumpversion.")
@click.option(
    "--bump-type", type=click.Choice(("patch", "minor", "major")), required=True
)
def cli(bump_type: str):  # pylint: disable=missing-function-docstring
    current = versioningit.get_version()
    current_match = _SEMVER.match(current)
    if not current_match:
        raise ValueError(f"Invalid version: {current}")
    result = current_match.groupdict()
    bump_version(result, bump_type)
    print(f"{result['major']}.{result['minor']}.{result['patch']}")


def bump_version(current_version: Dict[str, str], bump_type: str):
    current_version[bump_type] = str(int(current_version[bump_type]) + 1)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
