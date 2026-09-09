from storage import *
from task_manager import TaskManager

data = open_tasks()
manager = TaskManager()
manager.tasks = data["tasks"]
manager.next_id = data["next_id"]
manager.delete_task(1)
print(manager.tasks)
print(len(manager.tasks))


# TASK MANAGER MENU
def menu():
    print("=== TASK MANAGER ===")
    print("""
    1. Add task
    2. Show tasks
    3. Complete task
    4. Delete task
    5. Exit
    """)

# TASKS LIST
data = open_tasks()
tasks_list = data["tasks"]
next_id= data["next_id"]

# MENU CHOICE
while True:
    menu()

    # ERROR HANDLING
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Try again. \n" )
        continue

    # ADD TASK
    if choice == 1:
        while True:
            task = input("Enter your task: ")
            print("press q to exit")
            if task in ["q", "Q"]:
                break
            if task == "":
                print("Invalid task. Try again. \n" )
                continue

            task_data = {
                "task": task,
                "completed": False
            }

            tasks_list[next_id] = task_data
            next_id+=1
            data["tasks"] = tasks_list
            data["next_id"] = next_id
            write_tasks(data)

    # SHOW TASKS
    elif choice == 2:
        for num, task in tasks_list.items():
            if task["completed"]:
                print(f"{num}. [x] {task['task']}")
            else:
                print(f"{num}. [ ] {task['task']}")


    # COMPLETE TASK
    elif choice == 3:
            while True:
                completed_task = input("Enter number of task to complete: ")
                print("press q to exit")
                if completed_task in ["q", "Q"]:
                    break
                if completed_task.isdigit():
                    completed_task = int(completed_task)
                    if completed_task in tasks_list:
                        tasks_list[completed_task]["completed"] = True
                        write_tasks(data)
                    else:
                        print("Invalid number. Try again. \n" )
                else:
                    print("Invalid number. Try again. \n" )


    # DELETE TASK
    elif choice == 4:
        try:
            delete_task = int(input("Enter number of task to delete: "))
        except ValueError:
            print("Invalid number. Try again. \n" )
            continue
        if delete_task in tasks_list:
            del tasks_list[delete_task]
            write_tasks(data)
            print("Task deleted")

        else:
            print("Invalid number. Try again. \n" )


    # EXIT THE PROGRAM
    elif choice == 5:
        print("=== EXITING ===")
        break


    else:
        print("Invalid choice. Try again. \n" )
