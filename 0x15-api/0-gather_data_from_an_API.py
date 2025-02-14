#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys

# Check if employee ID argument is provided
if len(sys.argv) < 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

# Convert the argument to an integer
try:
    employee_id = int(sys.argv[1])
except ValueError:
    print("Error: The argument must be an integer.")
    sys.exit(1)

# Fetch employee details to get the employee name
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
user_response = requests.get(user_url)
if user_response.status_code != 200:
    print("Error: Could not retrieve user data")
    sys.exit(1)
user_data = user_response.json()
employee_name = user_data.get("name")

# Fetch the list of TODO tasks
todos_url = "https://jsonplaceholder.typicode.com/todos"
todos_response = requests.get(todos_url)
if todos_response.status_code != 200:
    print("Error: Could not retrieve todos data")
    sys.exit(1)
todos = todos_response.json()

# Filter tasks for the given employee ID
user_tasks = [task for task in todos if task.get("userId") == employee_id]
total_tasks = len(user_tasks)
completed_tasks = [task for task in user_tasks if task.get("completed")]
completed_count = len(completed_tasks)

# Print the progress summary and the titles of completed tasks
print(f"Employee {employee_name} is done with tasks\
({completed_count}/{total_tasks}):")
for task in completed_tasks:
    print(f"\t {task.get('title')}")
