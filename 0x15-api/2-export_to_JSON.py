#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(base_url + "users/{}".format(employee_id)).json()
    username = user_info.get("username")
    tasks = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({
            employee_id: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                } for task in tasks
            ]
        }, jsonfile)
