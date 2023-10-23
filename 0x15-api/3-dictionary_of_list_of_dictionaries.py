#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format
"""
import requests
import json


def export_all_as_json():
    """return api data"""
    base_url = "http://jsonplaceholder.typicode.com"
    user = requests.get(base_url + "/users")
    USERS = []
    for per in user.json():
        USERS.append((per.get("id"), per.get("username")))

    TASK_STATUS_TITLE = []
    to_do = requests.get(base_url + "/todos")
    for task in to_do.json():
        TASK_STATUS_TITLE.append((task.get("userId"), task.get("completed"),
                                   task.get("title")))

    data_dict = dict()
    for per in USERS:
        tasks = []
        for task in TASK_STATUS_TITLE:
            if task[0] == per[0]:
                tasks.append({"task": task[2], "completed": task[1],
                              "username": per[1]})
        data_dict[str(per[0])] = tasks

    file_name = "todo_all_employees.json"
    with open(file_name, "w") as f:
        json.dump(data_dict, f, sort_keys=True)


if __name__ == "__main__":
    export_all_as_json()
