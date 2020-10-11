import json

def greet_user():
    """Greet user by the name"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = json.load(f)
        with open (filename, 'w') as f:
            json.dump(username,f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
greet_user()