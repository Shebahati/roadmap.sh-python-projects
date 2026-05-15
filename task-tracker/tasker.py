from datetime import datetime
import json
import os

class Task:
    DATA_FILE = "tasks.json"
    all_tasks = [] 
    def __init__(self, desc):
        self.desc = desc
        self.id = len(self.all_tasks) + 1
        self.status = "todo"
        self.createdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updatedat = self.createdat
        Task.all_tasks.append(self.to_dict())
        Task._save()

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.desc,
            "status": self.status,
            "createdat": self.createdat,
            "updatedat": self.updatedat
        }

    @classmethod
    def _load(cls):
        if os.path.exists(cls.DATA_FILE):
            try:
                with open(cls.DATA_FILE, 'r', encoding='utf-8') as f:
                    cls.all_tasks = json.load(f)
            except (json.JSONDecodeError, IOError):
                cls.all_tasks = []
        else:
            cls.all_tasks = []
        cls._save()

    @classmethod
    def _save(cls):
        with open(cls.DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(cls.all_tasks, f, indent=4, ensure_ascii=False)

    @classmethod
    def add_task(cls, desc):
        for t in cls.all_tasks:
            if t["description"] == desc:
                return "This task already exists!"
        new_task = Task(desc)
        return f"Task added successfully (ID: {new_task.id})"

    @classmethod
    def update_task(cls, task_id, new_desc):
        for t in cls.all_tasks:
            if t["id"] == task_id:
                t["description"] = new_desc
                t["updatedat"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cls._save()
                return f"Task {task_id} updated successfully!"
        return "Task not found!"

    @classmethod
    def delete_task(cls, task_id):
        for i, t in enumerate(cls.all_tasks):
            if t["id"] == task_id:
                cls.all_tasks.pop(i)
                cls._save()
                return f"Task {task_id} deleted successfully!"
        return "Task not found!"

    @classmethod
    def update_status(cls, task_id, new_status):
        for t in cls.all_tasks:
            if t["id"] == task_id:
                t["status"] = new_status
                t["updatedat"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cls._save()
                return f"Task {task_id} marked as {new_status}!"
        return "Task not found!"

    @classmethod
    def list_tasks(cls, filter_status=None):
        if not filter_status:
            return cls.all_tasks
        return [t for t in cls.all_tasks if t["status"] == filter_status]

Task._load()