import tasker

with open("prompt.txt", "r", encoding="utf-8") as f:
    print(f.read())

def parse_command(cmd_str):
    if not cmd_str.startswith("task-cli "):
        return None, None, None
    rest = cmd_str[9:].strip()
    if not rest:
        return None, None, None

    parts = rest.split(maxsplit=1)
    action = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    task_id = None
    if action in ("update", "delete", "mark-in-progress", "mark-done"):
        id_part = arg.split(maxsplit=1)[0]
        if id_part.isdigit() and int(id_part) > 0:
            task_id = int(id_part)
          
            arg = arg[len(id_part):].strip()
        else:
            return action, None, arg
  
    if action in ("add", "update") and arg:
        if arg.startswith('"') and arg.endswith('"'):
            arg = arg[1:-1]

    return action, task_id, arg

dispatch = {
    "add": lambda tid, name: tasker.Task.add_task(name),
    "update": lambda tid, name: tasker.Task.update_task(tid, name) if tid else "Missing ID!",
    "delete": lambda tid, _: tasker.Task.delete_task(tid) if tid else "Missing ID!",
    "mark-in-progress": lambda tid, _: tasker.Task.update_status(tid, "in-progress") if tid else "Missing ID!",
    "mark-done": lambda tid, _: tasker.Task.update_status(tid, "done") if tid else "Missing ID!",
    "list": lambda _, status: tasker.Task.list_tasks(status if status else None),
}


while True:
    user_input = input("Enter your prompt: ").strip()
    if user_input == "q":
        break

    action, tid, arg = parse_command(user_input)
    if action is None:
        print("Invalid command format. Use: task-cli add/update/delete/...")
        continue

    if action in dispatch:
        result = dispatch[action](tid, arg)
        if isinstance(result, list):
            if not result:
                print("No tasks found.")
            else:
                print("ID | Description | Status | Created At | Updated At")
                for t in result:
                    print(f"{t['id']} | {t['description']} | {t['status']} | {t['createdat']} | {t['updatedat']}")
        else:
            print(result)
    else:
        print(f"Unknown action: {action}")