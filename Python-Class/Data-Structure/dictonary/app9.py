users = {
    "name": "Alice",
    "age": 25,
    "country": "United States"
}

users["age"] = 26
users["city"] = "New York"
users["country"] = "Canada"
users["email"] = "babyjoe@gmail.cum"
users.get("phone".capitalize(), "Not Provided")
print(f"Updated user info: {users}")