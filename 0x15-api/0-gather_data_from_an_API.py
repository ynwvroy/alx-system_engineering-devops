#!/usr/bin/python3
"""Script to gather data from a REST API for a given employee ID
and display TODO list progress.
"""

import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(f"{base_url}users/{employee_id}")
    user_data = user_response.json()

    # Fetch TODO list data
    todo_response = requests.get(f"{base_url}todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)

    # Display progress information
    print(f"Employee Name: {user_data['name']} is done with tasks "
          f"({completed_tasks}/{total_tasks}):")
    
    # Check if there are tasks to display
    if total_tasks > 0:
        for task in todo_data:
            # Display completed tasks
            if task['completed']:
                print(f"\t{task['title']}")
    else:
        print("\tNo tasks found for this employee.")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")

