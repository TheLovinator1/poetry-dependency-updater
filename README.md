# poetry-dependency-updater

Parses pyproject.toml for packages and runs `poetry add package@latest`
for each one.

Only works with packages from PyPI. Feel free to send
send pull requests to improve it.

## Usage

Needs [toml](https://pypi.org/project/toml/).

- Arch Linux:
  - `sudo pacman -S python-toml`
- Pip:
  - `pip install toml`
- Poetry:
  - `poetry add toml`
