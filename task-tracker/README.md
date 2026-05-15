# Task Tracker CLI

A simple CLI task manager from https://roadmap.sh/projects/task-tracker.

## Usage

Run `python main.py` then enter commands:

| Command | Description |
|---------|-------------|
| `task-cli add "task name"` | Add task |
| `task-cli update <id> "new name"` | Update task |
| `task-cli delete <id>` | Delete task |
| `task-cli mark-in-progress <id>` | Mark in-progress |
| `task-cli mark-done <id>` | Mark done |
| `task-cli list` | List all tasks |
| `task-cli list todo` / `done` / `in-progress` | Filter by status |
| `q` | Quit |

## Example

`task-cli add "Buy groceries"`
`task-cli list`
`task-cli mark-done 1`


## Requirements

Python 3.8+
