
fruits = ["apple", "banana", "orange", "mango", "grape"]

for fruit in fruits:
    if fruit == "orange":
        continue

    if fruit == "mango":
        break

    print(fruit)