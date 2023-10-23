#!/usr/bin/python3
"""uses REST APi for employee ID,returns info about usr TODO list progress
"""
import requests
from sys import argv


def show_todo():
    """displays todo list progress"""
    base_url = "https://jsonplaceholder.typicode.com"
    output = "Employee {} is done with tasks({}/{})"
    user = requests.get(base_url + "/users")
    for per in user.json():
        if per.get("id") == int(argv[1]):
            EMPLOYEE_NAME = (per.get("name"))
            break

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    to_do = requests.get(base_url + "/todos")
    for task in to_do.json():
        if task.get("userId") == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(task.get("title"))

    print(output.format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                        TOTAL_NUMBER_OF_TASKS))

    for t in TASK_TITLE:
        print("\t {}".format(t))


if __name__ == "__main__":
    show_todo()
