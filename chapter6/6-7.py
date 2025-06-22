# list people in seperate dictionaries and loop through them after placing them in a list

person = {'first name': 'Evan', 'last name': 'slaski', 'age': '28',
          'city': 'roanoke'}
person2 = {'first name': 'abby', 'last name': 'taylor', 'age': 31, 'city': 'roanoke'}
person3 = {'first name': 'jesse', 'last name': 'taylor', 'age': 33, 'city': 'summit'}

people = [person, person2, person3]
print(people)

for person in people:
    print(f'{person}')

# create many dictionaries that represent a different pet    
luna = {
    'breed': 'black lab',
    'owner': 'austin'
}

lucy = {
    'breed': 'black lab',
    'owner': 'ayers'
}

bens_dog = {
    'breed': 'cute dog',
    'owner': 'ben'
}

print('pets:')
pets = [luna, lucy, bens_dog]
for pet in pets:
    print(f'{pet}')
    
