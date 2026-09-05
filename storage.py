import json

#write tasks
def write_tasks(data):
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)


#read tasks
def open_tasks():
    with open("tasks.json", "r") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = {"tasks": {},"next_id": 1}

    #key conversion to int
    new_data = {}
    for id, task in data["tasks"].items():
        new_data[int(id)] = task

    data["tasks"] = new_data

    return data
