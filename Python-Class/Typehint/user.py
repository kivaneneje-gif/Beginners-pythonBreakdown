def create_user(name:str, age:int, gender:str) -> dict:
    user = {
        "name": name,
        "age": age,
        "gender": gender
    }
    print(f"User created: {name}, Age: {age}, Gender: {gender}")
    return user
user1 = create_user("Alice", 30, "Female")