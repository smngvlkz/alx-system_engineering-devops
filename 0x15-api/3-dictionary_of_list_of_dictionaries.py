#!/usr/bin/python3
"""Export all employee TODO data to JSON"""
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()

    todo_dict = {}
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        user_todos = requests.get(f'{url}/{user_id}/todos').json()
        
        todo_dict[user_id] = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in user_todos
        ]

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(todo_dict, jsonfile)
