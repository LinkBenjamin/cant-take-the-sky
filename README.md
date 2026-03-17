# Can't Take the Sky

Welcome to an unofficial Firefly game!  I wanted to do something to celebrate the attempts to revive the show, so... I made a game.

## Running the dev local version

- Clone the repository
- Have Python 3.12+
- Run:

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate # Change to /.venv/Scripts/activate if you're on a Windows box)

# Update pip
python -m pip --upgrade pip

# Install dependencies: note, your choices are 'dev', 'release', or 'all'
pip install -e .[all]

python src/app/main.py
```