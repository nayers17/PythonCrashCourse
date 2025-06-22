age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
    
print(f"You are {age} years old. Your admission cost is ${price}.")