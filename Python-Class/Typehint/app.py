def create_user(name: str, age: int):
    print(f"User created: {name}, Age: {age}")
create_user("Alice", 30)

def add (a: int, b: int):
    return f" the sum of {a} and {b} is {a + b}"

sum_result = add(5, 3)
print(sum_result)

def greet(name: str, greeting: str = "Hello", gender: str = "unknown"):

    print(f"Welcome {greeting}, {name}, Are you a {gender}!")

hi= greet("Alice", "Hi", "female") 