# 4-3
# numbers = list(range(21))
# for number in numbers:
#     print(number)

# 4-4    
numbers = list(range(1000001))
# for number in numbers:
#     print(number)

# 4-4    
print(max(numbers))
print(min(numbers))

# 4-5
print(sum(numbers))

# 4-6
odds = list(range(1, 20, 2))
for odd in odds:
    print(odd)
    
# 4-7
values = []
for value in list(range(0, 30, 3)):
    print(value)
    values.append(value)
    
print(values)

# 4-8
values = []
for value in list(range(10)):
    value = value ** 3
    values.append(value)
    
print(values)

# 4-9 List Comprehension
print([value ** 3 for value in list(range(10))])
