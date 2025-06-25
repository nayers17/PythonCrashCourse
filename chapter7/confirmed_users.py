# Moving items from one list to another

# Start with user that need to be verified
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify users until there are no more confirmed users
# Move each verified user into the list of confirmed users

while unconfirmed_users:
    # right here we are creating a variable to store the removed value from unconfirmed user list
    current_user = unconfirmed_users.pop()
    
    # next, we use the print function and embed the recently created variable that is storing the value of the popped
    # element to validate that current_user is holding the user that is getting verified
    print(f"\nVerifying user: {current_user.title()}")
    # Here, we are adding the user that is getting verified to the confirmed users list with "append()" on the list
    confirmed_users.append(current_user)
    # this loop will continue going until we run out of elements in the unconfirmed users list

    
print("\nThe following users have been confirmed:\n")
# next, we create a for loop that loops through the confirmed users
for confirmed_user in confirmed_users:
    #and we print out each confirmed user in the "confirmed users list"
    print(confirmed_user.title())

# validating pop and append methods worked as intended, and elements were removed from the unconfirmed list to the 
# confirmed list    
print(confirmed_users)
print(unconfirmed_users)


