# polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'george': 'python' 
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages:
#     print(f'\n{name.title()}')
    
# friends = ['phil', 'sarah']
# for name in favorite_languages:
#     print(f"Hi {name.title()}.")
    
#     if name in friends:
#         language = favorite_languages[name]
#         print(f'\t{name.title()}, I see you love {language}!')
        
# if 'erin' not in favorite_languages:
#     print(f'Erin, please take our poll!\n')

# for name in sorted(favorite_languages.keys()):
#     print(f'{name.title()}, thank you for taking this poll.\n')
    
# for value in sorted(favorite_languages.values()):
#     print(f'This value was entered in the poll: {value}')
    
# print('These are the unique languages gathered in the poll:')    
# for value in set(favorite_languages.values()):
#     print(value)
    
# languages = {'python', 'rust', 'python', 'c'}


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'george': 'python' 
}

should = ['abby', 'jesse', 'chloe', 'edward', 'jen']
print('List of people who should take the poll:')
for people in should:
    print(people.title())
    
    if people in favorite_languages.keys():
        print('\tWe see you already took the poll')
    elif people not in favorite_languages.keys():
        print('\tWe highly encourage you to take the poll to see what your favorite language is!')

