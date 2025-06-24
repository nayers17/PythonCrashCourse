# 5-11 ordinal numbers

# storing numbers  
numbers = list(range(1, 10))
print(numbers)

# looping through list
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

