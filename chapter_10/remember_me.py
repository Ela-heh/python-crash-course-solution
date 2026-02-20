from pathlib import Path
import json

def get_stored_name(path):
    if path.exists():
        contest = path.read_text()
        username = json.loads(contest)
        return username
    else:
        return None
    
def get_name(path):
    username = input("What is your name ? ")
    contest = json.dumps(username)
    path.write_text(contest)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_name(path)
    if username:
        print(f"Welcom back,{username}")

    else:
        username = get_name(path)
        print(f"We will remember u ,{username}!")

greet_user()