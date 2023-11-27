#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user_info = requests.get(base_url + "users/{}".format(employee_id)).json()
    tasks = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()

    completed_tasks = [task.get("title") for task in tasks
                       if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_info.get("name"), len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task))
