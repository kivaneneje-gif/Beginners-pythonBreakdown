digit = [1, 2, 3, 4, 5]
print(f"Original list: {digit[0]}")

user = ['Alice', 'Bob', 'Charlie']
user.append('David')
print(f"Updated list: {user}")
user.remove('Bob')
user.extend(['Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'])
print(f"Updated list after removing 'Bob' and extending user info: {user}")