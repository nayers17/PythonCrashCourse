prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished)\n\n"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    
    elif city == 'radford':
        print(f'\n{city.title()} is a beautiful city!')
        
    elif city == 'blacksburg':
        print(f'{city.title()} is not as good as Radford')
    
    else:
        print(f'{city.title()} is alright, but still not as good as Radford tbh')
        
