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
    
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name]
        print(f'\t{name.title()}, I see you love {language}!')
        
if 'erin' not in favorite_languages:
    print(f'Erin, please take our poll!\n')

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking this poll.\n')
    
for value in sorted(favorite_languages.values()):
    print(f'This value was entered in the poll: {value}')
    
print('These are the unique languages gathered in the poll:')    
for value in set(favorite_languages.values()):
    print(value)
    
languages = {'python', 'rust', 'python', 'c'}

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are: ")
    
    for language in languages:
        print(f'\t{language.title()}')
        
