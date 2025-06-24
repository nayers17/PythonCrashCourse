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
    
# three names to use as keys,     
favorite_places = {
    'abby': {
        'place1' : 'roanoke',
        'place2' : 'new york',
        'place3' : 'arkansas'
    },
    
    'jesse': {
        'place1': 'new york',
        'place2': 'charlotte',
        'place3': 'charlottesville'
    },
    
    'evan': {
        'place1': 'roanoke',
        'place2': 'charlotte',
        'place3': 'arkansas'
    }
}

for person in favorite_places:
    print(f'{favorite_places}')
    
    
# 6-10
# modify so each person can have more than one favorite number
# print each person's name along with their favorite numbers
fav_numbers = {'evan': '10', 'chloe': '2', 'jesse': '20', 'austin': '15'}
print(fav_numbers)

favorite_numbers = {
    'evan': {
        'fav number': 1,
        'second fav': 5,
        'third favorite': 10
    },
    
    'abby': {
        'fav number': 10,
        'second fav': 20,
        'third favorite': 9
    },
    
    'jesse': {
        'fav number': 3,
        'second fav': 10,
        'third favorite': 33
    }
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are: {numbers['fav number']}, "
          f"{numbers['second fav']}, and {numbers['third favorite']} in order.")
    
# 6-11
# use three names of cities as keys, includ the country, population, and a fun fact
#
cities = {
    'Miami': {
        'country': 'United States',
        'population': '455,924', 
        'fact': 'only major city founded by a woman'
    },
    
    'Charlotte': {
        'country': 'United States',
        'population': '911,311',
        'fact': 'Known as a financial capital'
    },
    
    'New York City': {
        'country': 'United States',
        'population': '8,258,000',
        'fact': 'largest city in the United States'
    }
}   

for city, info in cities.items():
    print(f'City: {city} - Country: {info['country']}, '
          f'\nPopulation: {info['population']}, Fact: {info['fact']}')
    
cities = {
    'Miami': {
        'country': 'United States',
        'population': '455,924', 
        'fact': ['only major city founded by a woman', '30 minutes away from me']
    },
    
    'Charlotte': {
        'country': 'United States',
        'population': '911,311',
        'fact': ['Known as a financial capital', 'lots of fresh post-grads']
    },
    
    'New York City': {
        'country': 'United States',
        'population': '8,258,000',
        'fact': ['largest city in the United States', 'statue of liberty location']
    }
}  

for city, info in sorted(cities.items()):
    if city == 'Miami':
        print(f'\nName of city: {city}')
        print(f"Located: {info['country']}\nPopulation: {info['population']}")
        for info in info['fact']:
            print(f'Fun fact about {city}: {info}')
    
    elif city == 'Charlotte':
        print(f'\nName of city: {city}')
        print(f"Located: {info['country']}\nPopulation: {info['population']}")
        for info in info['fact']:
            print(f'Fun fact about {city}: {info}')
    
    else:
        print(f'\nName of city: {city}')
        print(f"Located: {info['country']}\nPopulation: {info['population']}")
        for info in info['fact']:
            print(f'Fun fact about {city}: {info}')    