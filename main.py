from storage import *
from task_manager import TaskManager

manager = TaskManager()

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
manager.tasks = data["tasks"]
manager.next_id = data["next_id"]

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

            manager.add_task(task)
            write_tasks(manager)

    # SHOW TASKS
    elif choice == 2:
        for num, task in enumerate(manager.tasks, start = 1):
            if task.completed:
                print(f"{num}. [x] {task.task}")
            else:
                print(f"{num}. [ ] {task.task}")


    # COMPLETE TASK
    elif choice == 3:
            while True:
                completed_task = input("Enter number of task to complete: ")
                print("press q to exit")
                if completed_task in ["q", "Q"]:
                    break

                if completed_task.isdigit():
                    completed_task = int(completed_task)

                    if 0 < completed_task <= len(manager.tasks):
                        manager.complete_task(manager.tasks[completed_task-1].id)
                        write_tasks(manager)
                    else:
                        print("Invalid number. Try again. \n" )

                else:
                    print("Invalid number. Try again. \n" )


    # DELETE TASK
    elif choice == 4:
        try:
            task_number = int(input("Enter number of task to delete: "))
        except ValueError:
            print("Invalid number. Try again. \n" )
            continue
        if 0 < task_number <= len(manager.tasks):
            manager.delete_task(manager.tasks[task_number -1].id)
            write_tasks(manager)
            print("Task deleted")

        else:
            print("Invalid number. Try again. \n" )


    # EXIT THE PROGRAM
    elif choice == 5:
        print("=== EXITING ===")
        break


    else:
        print("Invalid choice. Try again. \n" )
