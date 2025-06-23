# 7-1 
# print a message that requests what type of car they're interested in renting, and print a response with the 
# preferred car type and say you'll look for it

carpreference = input("What type of rental car are you interested in acquiring? ")

print(f"\nExcellent, let me see if I can find you a {carpreference} to rent.")

# 7-2: Restaurant Seating
# Ask the user how many people are in their dinner group
# if the answer is more than 8, print a message saying they'll have to wait for a table
# If if is less than 8, say their table is ready

amount = input("Welcome, how many people will be at your table? ")
amount = int(amount)

if amount >= 8:
    print(f"Sorry, since you have {amount} people, you will be required to wait for a larger table. Anything less than 8 is immediate seating.")
else: 
    print(f'You said {amount} people? Right this way!')

# 7-3
# Ask user for a number, report if it is a multiple of 10 or not

number = input("Please provide a number to see if it is divisible by 10: ")
number = int(number)

if number % 10 == 0:
    print(f"Your number, {number} is divisible by 10!")
else:
    print(f'The number you entered, {number}, is not divisible by 10.')
    
