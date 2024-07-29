#!/usr/bin/python3
"""Export API data to JSON"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id
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

    json_data = {user_id: tasks}
    with open(f'{user_id}.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile)
