users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einsten',
        'location': 'princeton'
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

# print(users['aeinstein'])

for username, user_info in users['aeinstein'].items():
    print(f'{username.title()}: {user_info.title()}')
    
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = f"{user_info['location'].title()}"
    
    print(f"The user's full name is: {full_name}\nTheir location is: {location}")
    
