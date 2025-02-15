#!/usr/bin/python3
"""
Fetches and exports data in JSON format.
Exports all tasks from all employees to a JSON file.
"""

import json
import requests


def fetch_data():
    """Fetch user and todo data from API."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    return users, todos


def format_data(users, todos):
    """Formats fetched data into the required JSON structure."""
    data = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        data[user_id] = []

        for task in todos:
            if task['userId'] == user_id:
                data[user_id].append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })

    return data


def save_to_json(data, filename="todo_all_employees.json"):
    """Saves formatted data to a JSON file."""
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    users, todos = fetch_data()
    formatted_data = format_data(users, todos)
    save_to_json(formatted_data)
