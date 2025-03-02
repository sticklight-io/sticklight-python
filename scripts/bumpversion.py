#!uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "semver",
#     "tomli",
# ]
# ///

"""
Usage: ./scripts/bumpversion [-y]

Will confirm whether to bump the version unless -y flag is provided.
"""

import re
import sys
from pathlib import Path

import semver
import tomli


def main():
    skip_confirmation = "-y" in sys.argv[1:]

    # Read current version from pyproject.toml
    with Path("pyproject.toml").open("r") as f:
        pyproject_str = f.read()
    pyproject_dict = tomli.loads(pyproject_str)

    current_version = pyproject_dict["project"]["version"]
    new_version = str(semver.VersionInfo.parse(current_version).bump_patch())

    # Get user confirmation unless -y flag is provided
    if not skip_confirmation:
        response = (
            input(
                f"Are you sure you want to bump the version from {current_version} to {new_version}? (y/n): "
            )
            .lower()
            .strip()
        )
        if response != "y":
            sys.exit(1)

    # Update version in pyproject.toml
    pyproject_str = re.sub(
        r"version *= *\"(.*)\"", f'version = "{new_version}"', pyproject_str
    )

    with Path("pyproject.toml").open("w") as f:
        f.write(pyproject_str)

    # Confirm that the version was updated
    with Path("pyproject.toml").open("r") as f:
        actual_version = tomli.loads(f.read())["project"]["version"]
        assert actual_version == new_version, (
            f"Version was not updated in pyproject.toml. Expected {new_version}, got {actual_version}"
        )

    print(f"✅ Bumped version from {current_version} to {new_version}")


if __name__ == "__main__":
    main()
