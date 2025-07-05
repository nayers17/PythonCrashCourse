def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f'I have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('black lab', 'lucy')
describe_pet('cat', 'jerome')
describe_pet(animal_type='dog', pet_name='craig')
describe_pet(pet_name='craig', animal_type='dog')

def describe_dog(pet_name, animal_type='dog'):
    print(f"My {animal_type}'s name is {pet_name}")
    
describe_dog('Leroy')

describe_dog('clyde', animal_type='cat')

