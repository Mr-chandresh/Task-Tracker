def show_tasks(tasks, status_filter=None):
    for i, task in enumerate(tasks):
        if status_filter is None or task["status"] == status_filter:
            print(i + 1, task["task"], "-", task["status"])
