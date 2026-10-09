def calculate_total(price: float, quantity: int) -> float:
   return price * quantity

def calculate_discounted_total(total: float,) -> float:
   return total * 0.9  # Apply a 10% discount

def calculate_final_total(price: float, quantity: int) -> float:
   total = calculate_total(price, quantity)
   discounted_total = calculate_discounted_total(total)
   return total - discounted_total

cost = calculate_final_total(500, 5)
print(f"Final total after discount: {cost}")

