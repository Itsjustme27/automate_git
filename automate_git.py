import requests
import json
import os

# Your GitHub personal access token
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = input('Enter your username: ')

# Function to create a GitHub Repo
def create_github_repo(repo_name, description='', private=True):
    url = 'https://api.github.com/user/repos'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {
        'name': repo_name,
        'description': description,
        'private': private
    }
    response = requests.post(url, headers=headers, json=payload)  # Use 'json=' instead of 'data=json.dumps()'
    
    if response.status_code == 201:
        print(f'Successfully created repository {repo_name}')
        print(f'Status code: {response.status_code}, Response: {response.text}')
        return response.json()['clone_url']  # Return the clone URL for the new repo
    else:
        print(f'Failed to create repository: {response.text}')  # Print error message
        return None

repo_name = input('Enter your repo name: ')
description = input('Write a short Description: ')
repo_url = create_github_repo(repo_name, description)

if repo_url:
    # Define the local path
    clone_path = os.path.join(os.path.expanduser('~'), 'Documents', 'github',  repo_name)
    # Clone the repo locally
    os.system(f'git clone {repo_url} {clone_path}')
    print(f'Cloned {repo_name} into {clone_path}')
else:
    print('Repository creation failed. Clone operation skipped.')
