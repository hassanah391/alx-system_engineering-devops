#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list
and exports it to a JSON file.
"""

import json
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

# Fetch employee details to get the employee username
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
user_response = requests.get(user_url)
if user_response.status_code != 200:
    print("Error: Could not retrieve user data")
    sys.exit(1)
user_data = user_response.json()
employee_username = user_data.get("username")

# Fetch the list of TODO tasks
todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
todos_response = requests.get(todos_url)
if todos_response.status_code != 200:
    print("Error: Could not retrieve todos data")
    sys.exit(1)
todos = todos_response.json()

# Format the data
user_tasks = [
    {"task": task["title"], "completed": task["completed"],
     "username": employee_username}
    for task in todos
]

# Create the final dictionary structure
output_data = {str(employee_id): user_tasks}

# Write to a JSON file
json_filename = f"{employee_id}.json"
with open(json_filename, 'w') as json_file:
    json.dump(output_data, json_file)
