users = []

def add_user(name: str, age: int) -> dict:
    user = {
        "id": len(users) + 1,
        "name": name,
        "age": age
    }
    users.append(user)
    return user

user1 = add_user("Alice", 25)
user2 = add_user("Bob", 30)
user3 = add_user("Charlie", 22)
print(f"Users added: {user1}, {user2}, {user3}")

def get_user(user_id: int) -> dict | None:
    for user in users:
        if user["id"] == user_id:
            return user
    return None

user = get_user(2)
print(f"User with ID 2: {user}")