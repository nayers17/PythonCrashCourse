#7-4

# pizza toppings
# write a loop that prompts the user to enter a series of pizza toppings until they type 'quit'
# after they enter each topping, pring a message saying you'll add that topping


# print("Type 'quit' to exit the program\n\n")

# order = ("Tell me the pizza toppings in you want on your pizza: ")

# topping = ''
# while topping != 'quit':
#     topping = input(order)
    
#     if topping == 'quit':
#         break
    
#     elif topping != 'quit':
#         print(f"Adding {topping.title()} to your pizza!\n")
        
# 7-5

# ask a user their age and then tell them the cost of their ticket based off their age
# ticket = free if age < 3
# ticket = $10 if age > 3 and < 12
# ticket = $15 if age > 12


# prompt = "Enter your age so I can tell you how much your ticket will be: "

# active = True
# while active: 
#     age = int(input(prompt))

#     if age < 3:
#         print("Your ticket will be free!")
        
#     elif age >=3 and age < 12:
#         print('Your ticket will be $10!')
        
#     elif age >= 12:
#         print("Your ticket will be $15!")
        
#     elif age == 'quit':
#         break

# 7-5
# use break to exit the while loop

while True:
    entry = input("Enter your age to see how much your movie ticket will be: (or enter 'quit' to quit) ")
    if entry == 'quit':
        break
    age = int(entry)
    
    if age < 3:
        price = 0
        
    elif age >=3 and age < 12:
        price = 10
        
    elif age >= 12:
        price = 15
    
    print(f"Your ticket will be ${price}!\n")
    
# use active to exit the while loop

active = True
while active:
    request = input("\nEnter in the pizza topping you would like:\nType 'q' to exit\n\n")
    if request == 'q':
        break
    
    else:
        print(f"Your pizza with {request} is coming up!\n")
        
# 7-7: Infinity

# Write a loop that never ends

x = 0
while True:
    x += 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
    print(x)
    
