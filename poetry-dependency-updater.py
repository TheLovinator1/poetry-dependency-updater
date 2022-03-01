#!/usr/bin/python

import subprocess
import sys

import toml

with open("pyproject.toml", encoding="utf-8") as f:
    # Parse the TOML file
    pyproject = toml.load(f)

    # Get dependencies
    dependencies = pyproject["tool"]["poetry"]["dependencies"]
    for dep in dependencies:
        extras = ""
        dep_version = dependencies[dep]

        # Don't try to update python
        if dep == "python":
            continue

        # If the dependency is a git dependency, don't update it
        # TODO: Add support for git dependencies
        if "git" in dep_version:
            print(f"{dep}: {dep_version} is a git dependency, skipping")
            continue

        # Check if dependency has extra dependencies
        # Example: uvicorn = { extras = ["standard"], version = "^0.17.5" }
        if "extras" in dep_version:
            extras = dep_version["extras"]

        # Update the dependency
        try:
            cmd = f"poetry add {dep}{extras}@latest"
            print(f"Running: {cmd}")
            subprocess.run(
                cmd,
                check=True,
                text=True,
                shell=True,
            )
        except subprocess.CalledProcessError as e:
            sys.exit(f"Failed for {dep}\n{e}")

# Run a extra 'poetry update' for fun
try:
    cmd = "poetry update"
    print(f"Running: {cmd}")
    subprocess.run(
        cmd,
        check=True,
        text=True,
        shell=True,
    )
except subprocess.CalledProcessError as e:
    sys.exit(f"Failed to run final update\n{e}")
