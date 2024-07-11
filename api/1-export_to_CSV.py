#!/usr/bin/python3
"""Fetches employee data and exports TODO list to CSV file"""

import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee and todo data from the API."""
    base_url = f"https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return None, None

    return user_response.json(), todos_response.json()


def export_to_csv(employee_id, employee, todos):
    """Export the TODO list data to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee.get('username'),
                task.get('completed'),
                task.get('title')
            ])
    print(f"Data exported to {filename}")


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

export_to_csv(employee_id, employee, todos)
