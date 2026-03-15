## Scholar
Terminal based education assistant to log tests and help set targets.
Compatible with todo to-do list (https://github.com/demtellme/todo.git)

Mainly made for personal use but made available for anyone to use for practice.
Commands are intentionally verbose — you should be conscious of what you're logging.

Basically abandoned, wont be updated much.

## Installation
```bash
# Recommended
pipx install git+https://github.com/demtellme/scholar.git

# Or with pip
pip install --user git+https://github.com/demtellme/scholar.git
```

## Uninstall
```bash
pipx uninstall scholar
```

## Usage
```bash
scholar <command>
```

## Commands
- `log` - logs a test, what went well and what can be improved
- `fback` - displays feedback from the last week without logging anything
- `tgt` - adds targets to a text file based on logged tests, uses todo list if active

Made by Alex G
>>>>>>> 4c2ec6f (Version 1 - Log function, more functions planned out that will be added later. Changed the layout of the project)
