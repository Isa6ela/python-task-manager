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

#TASKS LISTS
tasks_list = {}

# MENU CHOICE
while True:
    menu()

    choice = int(input("Enter your choice: "))
    #ADD TASK
    if choice == 1:
        while True:
            task = input("Enter your task: ")
            print("press q to exit")
            if task == "q":
                break
            number = len(tasks_list)+1
            tasks_list[number] = task

    #SHOW TASKS
    elif choice == 2:
        for num, task in tasks_list.items():
            print(f"{num}.[ ] {task}")

    #COMPLETE TASK
    # elif choice == 3:
    #         while True:
    #             completed_task = input("Enter number of your completed task: ")
    #             print("press q to exit")
    #             if completed_task == "q":
    #                 break
    #             elif completed_task in tasks_list:




    #DELETE TASK
    elif choice == 4:
        delete_task = int(input("Enter number of task to delete: "))
        if delete_task in tasks_list:
            del tasks_list[delete_task]

            new_tasks_list = {}
            for new_number, task in enumerate(tasks_list.values(), start = 1):
                new_tasks_list[new_number] = task

            tasks_list = new_tasks_list

            print("Task deleted")


    # EXIT THE PROGRAM
    elif choice == 5:
        print("=== EXITING ===")
        break

