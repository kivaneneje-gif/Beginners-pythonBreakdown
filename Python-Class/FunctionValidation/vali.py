
def user(age: int, name: str, gender: str) -> dict:
   if age < 21:
      return{
         "error": "user must atleast be 21 years old"
      }
   return{
      "name": name,
      "age": age,    
      "gender": gender
   }
user1 = user(19, "Alice", "Female")
if "error" in user1:
   print(f"Error: {user1['error']}")
else:
   print(f"User created: {user1['name']}, Age: {user1['age']}, Gender: {user1['gender']}")