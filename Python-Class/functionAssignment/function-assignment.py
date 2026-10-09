# ==========================================
# PYTHON FUNCTIONS ASSIGNMENT
# Functions, Parameters, Return Values,
# Type Hints & Lambda
# ==========================================


# ==========================================
# TASK 1 — STUDENT GRADE CALCULATOR
# ==========================================

def calculate_grade(score: int) -> str:
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


# Testing Task 1

print("===== TASK 1 =====")
print(calculate_grade(85))
print(calculate_grade(62))
print(calculate_grade(55))
print(calculate_grade(47))
print(calculate_grade(35))


# ==========================================
# TASK 2 — USER CREATION & VALIDATION
# ==========================================

def create_user(name: str, age: int, country: str = "Chinese") -> dict:
    if name == "":
        return {"error": "Name is required"}

    if age < 18:
        return {"error": "User must be 18 or older"}

    return {
        "name": name,
        "age": age,
        "country": country
    }


# Testing Task 2

print("\n===== TASK 2 =====")

# Valid user
print(create_user("James", 28, "United States"))

# User below 18
print(create_user("John", 16, "Canada"))

# Empty name
print(create_user("", 25, "China"))

# Country not provided
print(create_user("Mary", 30))


# ==========================================
# TASK 3 — SIMPLE USER MANAGEMENT SYSTEM
# ==========================================

users = [
    {"id": 1, "name": "James", "age": 28},
    {"id": 2, "name": "John", "age": 22},
    {"id": 3, "name": "Mary", "age": 25}
]


# 1. Get User

def get_user(user_id: int) -> dict | None:
    for user in users:
        if user["id"] == user_id:
            return user

    return None


# 2. Get Adult Users

def get_adults(users: list[dict]) -> list[dict]:
    adults = []

    for user in users:
        if user["age"] >= 18:
            adults.append(user)

    return adults


# 3. Add User

def add_user(users: list[dict], name: str, age: int) -> dict:
    new_id = len(users) + 1

    new_user = {
        "id": new_id,
        "name": name,
        "age": age
    }

    users.append(new_user)

    return new_user


# Testing Task 3

print("\n===== TASK 3 =====")

print("Get User:")
print(get_user(2))

print("User that does not exist:")
print(get_user(10))

print("Adult Users:")
print(get_adults(users))

print("Adding a new user:")
new_user = add_user(users, "David", 24)

print(new_user)
print(users)


# ==========================================
# TASK 4 — BACKEND-STYLE MINI PROJECT
# ==========================================

users = []


def create_backend_user(name: str, age: int) -> dict:
    new_id = len(users) + 1

    user = {
        "id": new_id,
        "name": name,
        "age": age
    }

    users.append(user)

    return user


def get_backend_user(user_id: int) -> dict | None:
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def get_all_users() -> list[dict]:
    return users


def delete_user(user_id: int) -> bool:
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return True

    return False


# Testing Task 4

print("\n===== TASK 4 =====")

print("Creating users:")
print(create_backend_user("James", 28))
print(create_backend_user("Sarah", 22))
print(create_backend_user("David", 19))

print("\nGet User:")
print(get_backend_user(2))

print("\nAll Users:")
print(get_all_users())

print("\nDelete User:")
print(delete_user(2))

print("\nUsers after deletion:")
print(get_all_users())

print("\nTry deleting a user that does not exist:")
print(delete_user(99))


# ==========================================
# BONUS — LAMBDA
# ==========================================

sorted_users = sorted(users, key=lambda user: user["age"])

print("\n===== BONUS — USERS SORTED BY AGE =====")
print(sorted_users)