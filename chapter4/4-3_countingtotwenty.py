# # numbers = list(range(21))
# # for number in numbers:
# #     print(number)
    
# numbers = list(range(1000001))
# # for number in numbers:
# #     print(number)
    
# print(max(numbers))
# print(min(numbers))

# odds = list(range(1, 20, 2))
# for odd in odds:
#     print(odd)

values = []
for value in list(range(0, 30, 3)):
    print(value)
    values.append(value)
    
print(values)


values = []
for value in list(range(10)):
    value = value ** 3
    values.append(value)
    
print(values)


print([value ** 3 for value in list(range(10))])
