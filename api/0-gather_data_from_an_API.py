#!/usr/bin/python3
"""Module to gather data from an API and display TODO list progress"""

import requests
import sys


def get_employee_todo_list(employee_id):
    """Fetch and display TODO list progress for a given employee ID."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(url)
    if user_response.status_code != 200:
        print(f"User with id {employee_id} not found")
        return

user = user_response.json()
name = user['name']
