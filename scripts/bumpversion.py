#!uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "semver",
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


def main():
    skip_confirmation = "-y" in sys.argv[1:]

    # Read current version from pyproject.toml
    with Path("pyproject.toml").open("r") as f:
        pyproject = f.read()

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
    pyproject = re.sub(
        r"version *= *\"(.*)\"", f'version = "{new_version}"', pyproject
    )

    with Path("pyproject.toml").open("w") as f:
        f.write(pyproject)

    print(f"Bumped version from {current_version} to {new_version}")


if __name__ == "__main__":
    main()
