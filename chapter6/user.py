# looping through key value pairs
# - write names for two variables that will hold the key and value

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')