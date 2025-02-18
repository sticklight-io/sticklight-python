#!uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "semver",
#     "tomli",
#     "tomli-w",
# ]
# ///

"""
Usage: ./scripts/bumpversion [-y]

Unless -y is provided, the script will confirm the version bump with the user before
writing the new version to pyproject.toml.
"""

import sys
from pathlib import Path

import semver
import tomli
import tomli_w


def main():
    # Check if -y flag is provided
    skip_confirmation = "-y" in sys.argv[1:]

    # Read current version from pyproject.toml
    with Path("pyproject.toml").open("rb") as f:
        pyproject = tomli.load(f)

    current_version = pyproject["project"]["version"]
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
    pyproject["project"]["version"] = new_version
    with Path("pyproject.toml").open("wb") as f:
        tomli_w.dump(pyproject, f)

    print(f"Bumped version from {current_version} to {new_version}")


if __name__ == "__main__":
    main()
