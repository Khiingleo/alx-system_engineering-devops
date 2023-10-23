#!/usr/bin/python3
"""
using task #0 extend the Python script to export data in the JSON format.
"""

import json
from sys import argv
import requests


def export_to_json():
    """returns data in json  format"""
    base_url = "http://jsonplaceholder.typicode.com"

    users = requests.get(base_url + "/users")
    for per in users.json():
        if per.get("id") == int(argv[1]):
            USERNAME = per.get("username")
            break

    TASK_STATUS_TITLE = []
    to_do = requests.get(base_url + "/todos")
    for task in to_do.json():
        if task.get("userId") == int(argv[1]):
            TASK_STATUS_TITLE.append((task.get("completed"),
                                      task.get("title")))

    task_list = []
    for task in TASK_STATUS_TITLE:
        task_list.append({"task": task[1], "completed": task[0],
                          "username": USERNAME})

    api_data = {str(argv[1]): task_list}
    file_name = "{}.json".format(argv[1])
    with open(file_name, "w") as f:
        json.dump(api_data, f)


if __name__ == "__main__":
    export_to_json()
