# Rivers

rivers = {'nile': 'egypt', 'mississippi': 'united states', 'amazon': 'brazil'}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')
    
for river in rivers.keys():
    print(river.title())
    
for river in rivers.values():
    print(river.title())