# HaxBallGym

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

HaxBallGym is a Python package that can be used to treat the game [HaxBall](https://www.haxball.com) as though it were an [OpenAI Gym](https://gym.openai.com)-style environment for Reinforcement Learning projects.

## Requirements

- Python >= 3.10

## Installation

Install the library via pip:

```bash
pip install haxballgym
```

That's it! Run `example.py` to see if the installation was successful. The script assumes you have a recordings folder from where you run the script.

## Use a local `ursinaxball`

If you maintain your own `ursinaxball` locally and want HaxBallGym to use it instead of downloading the PyPI dependency, you have two easy options.

- Poetry path dependency (recommended if using Poetry):

	1. Edit [pyproject.toml](pyproject.toml) and change the `ursinaxball` dependency to a local path:

		 ```toml
		 [tool.poetry.dependencies]
		 python = ">=3.10,<3.11"
		 numpy = "^1.23.5"
		 gym = "^0.26.2"
		 ursinaxball = { path = "../ursinaxball", develop = true }
		 ```

		 Adjust the path to where your `ursinaxball` source lives. Then reinstall:

		 ```bash
		 poetry install
		 ```

- Pip editable install (if not using Poetry workflows):

	```bash
	pip uninstall -y ursinaxball
	pip install -e /path/to/your/ursinaxball
	```

To verify the local package is being used:

```bash
python -c "import ursinaxball, sys; print(ursinaxball.__file__)"
```

It should print a path inside your local `ursinaxball` directory.

## Recordings

To watch recordings, go to my [HaxBall clone](https://wazarr94.github.io/) and load the recording file.

## Discord

[![Join our Discord server!](https://invidget.switchblade.xyz/TpKPeCe7y6)](https://discord.gg/TpKPeCe7y6)
