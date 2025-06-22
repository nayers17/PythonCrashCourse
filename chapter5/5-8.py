usernames = ['admin', 'nathan', 'evan', 'leslie', 'barthalamule']

for username in usernames:
    if username == 'admin':
        print(f'Hello {username.title()}, would you like to see a status report?')
    elif username == 'nathan':
        print(f'Hello {username.title()}, thank you for logging in again.')
    elif username == 'evan':
        print(f'Hello {username.title()}, thank you for logging in again.')
    elif username == 'leslie':
        print(f'Hello {username.title()}, thank you for logging in again.')
    elif username == 'barthalamule':
        print(f'Hello {username.title()}, thank you for logging in again.')
        
        
usernames = []
        
if username in usernames:
    print(f"Hi, {username}. Thanks for coming back!")
else:
    print("No user found.")
    
