#!/usr/bin/python3
"""Module to gather data from an API and display TODO list progress"""

import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee and todo data from the API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return None, None

    return user_response.json(), todos_response.json()


def display_todo_list_progress(employee, todos):
    """Display the todo list progress for the given employee."""
    name = employee.get('name')
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    done_count = len(done_tasks)

    print(f"Employee {name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee, todos = fetch_employee_data(employee_id)
    if not employee:
        print(f"User with id {employee_id} not found")
        sys.exit(1)

    display_todo_list_progress(employee, todos)
