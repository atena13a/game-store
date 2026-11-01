users = []

def register_user(username, password):
    user = {
        "username": username,
        "password": password
    }
    users.append(user)
    print("User registered successfully!")

def show_users():
    for user in users:
        print(user["username"])
