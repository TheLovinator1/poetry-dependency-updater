# poetry-dependency-updater

Parses pyproject.toml for packages and runs `poetry add package@latest`
for each one.

Needs [toml](https://pypi.org/project/toml/). Does not work with things outside PyPI. Feel free to send
send pull requests to improve it.

`sudo pacman -S python-toml` if you're using Arch Linux.
