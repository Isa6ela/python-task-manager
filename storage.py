import json
from task import Task

#write tasks
def write_tasks(manager):
    with open("tasks.json", "w") as file:
        new_data = []
        for task in manager.tasks:
            new_task = {"id": task.id, "task": task.task, "completed": task.completed}
            new_data.append(new_task)

        data = {"tasks": new_data, "next_id": manager.next_id}

        json.dump(data, file, indent=4)


#read tasks
def open_tasks():
    with open("tasks.json", "r") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = {"tasks": [], "next_id": 1}

    new_data = []
    for task in data["tasks"]:
        new_task = Task(task["id"], task["task"], task["completed"])
        new_data.append(new_task)

    data["tasks"] = new_data
    return data
