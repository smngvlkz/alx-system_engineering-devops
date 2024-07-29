#!/usr/bin/python3
"""Export API data to JSON"""
import json
import requests
import sys

if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    user = requests.get(url).json()
    username = user.get('username')
    todos = requests.get(url + '/todos').json()

    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })

    json_data = {USER_ID: tasks}
    with open(f'{USER_ID}.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile)
