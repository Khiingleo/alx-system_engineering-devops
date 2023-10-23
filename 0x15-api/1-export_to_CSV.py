#!/usr/bin/python3
"""
using task #0, extend the python script to export data in
CSV format
"""

import csv
import requests
from sys import argv


def export_in_csv():
    """return data in csv format"""
    base_url = "http://jsonplaceholder.typicode.com"
    users = requests.get(base_url + "/users")

    for per in users.json():
        if per.get("id") == int(argv[1]):
            USERNAME = (per.get("username"))
            break

    TASK_STATUS_TITLE = []
    to_do = requests.get(base_url + "/todos")
    for task in to_do.json():
        if task.get("userId") == int(argv[1]):
            TASK_STATUS_TITLE.append((task.get("completed"),
                                      task.get("title")))

    file_name = "{}.csv".format(argv[1])

    with open(file_name, "w") as csvfile:
        fields = ["USER_ID", "USERNAME",
                  "TASK_COMPLETED_STATUS", "TASK_TITLE"]

        writer = csv.DictWriter(csvfile, fieldnames=fields,
                                quoting=csv.QUOTE_ALL)

        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    export_in_csv()
