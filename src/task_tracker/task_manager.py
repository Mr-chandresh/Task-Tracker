def add_task(tasks, name):
    tasks.append({"task": name, "status": "Not started"})


def update_task(tasks, index, new_name):
    tasks[index]["task"] = new_name


def delete_task(tasks, index):
    tasks.pop(index)


def change_status(tasks, index, status):
    tasks[index]["status"] = status
