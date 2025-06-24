## Checking usernames

# creating a current user list
current_users = ['abby', 'chloe', 'keith', 'ted', 'jenny']

# creating a new user list
new_users = ['ChLoe', 'austin', 'samantha', 'bigs', 'keith']

# creating a for loop that loops through new users
for new_user in new_users:
    # checks new user is in current user list, AND new_user lowercase
    if new_user.lower() in current_users:
        print(f"{new_user} is already an active user. Please enter a new name.")
        
