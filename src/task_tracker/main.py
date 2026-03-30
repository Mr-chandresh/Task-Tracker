import sys

from display import show_tasks
from storage import load_tasks, save_tasks
from task_manager import add_task, change_status, delete_task, update_task

print("WELCOME TO TASK TRACKER")

tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Change Task Status")
    print("5. Show All Tasks")
    print("6. Show Done Tasks")
    print("7. Show Not Started Tasks")
    print("8. Show In Progress Tasks")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter task name: ")
        add_task(tasks, name)
        save_tasks(tasks)
        print("Task added successfully")

    elif choice == "2":
        show_tasks(tasks)
        n = int(input("Enter task number: ")) - 1
        new_name = input("Enter new task name: ")
        update_task(tasks, n, new_name)
        save_tasks(tasks)
        print("Task updated")

    elif choice == "3":
        show_tasks(tasks)
        n = int(input("Enter task number: ")) - 1
        delete_task(tasks, n)
        save_tasks(tasks)
        print("Task deleted")

    elif choice == "4":
        show_tasks(tasks)
        n = int(input("Enter task number: ")) - 1

        print("1. Not started")
        print("2. In progress")
        print("3. Done")

        s = input("Choose status: ")

        status = {
            "1": "Not started",
            "2": "In progress",
            "3": "Done",
        }

        if s in status:
            change_status(tasks, n, status[s])
            save_tasks(tasks)
            print("Status updated")

    elif choice == "5":
        show_tasks(tasks)

    elif choice == "6":
        show_tasks(tasks, "Done")

    elif choice == "7":
        show_tasks(tasks, "Not started")

    elif choice == "8":
        show_tasks(tasks, "In progress")

    elif choice == "9":
        print("Goodbye")
        sys.exit()

    else:
        print("Invalid choice")
