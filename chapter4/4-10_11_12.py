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


# 4-10 slices
print(f"The first three items in the list are: {numbers[0:3]}")
print(f"Three items from the middle of the list are: {numbers[9:12]}")
print(f"The last three items in the list are: {numbers[18:21]}")

# 4-11 My Pizzas, Your Pizzas


pizzas = ['cheese', 'bacon', 'sausage', 'pineapple']

for pizza in pizzas:
    print(f"I love {pizza} pizza!")

print(f"\n{pizzas[0].title()} pizza is a go to pizza and never fails.\n{pizzas[1].title()} pizza is a slept on and doesn't get enough credit.\n{pizzas[2].title()} pizza can either be hit or miss - it depends on the sausage.\n{pizzas[2].title()} pizza is controversial, but I stand with {pizzas[2]} pizza!")

# 4-12

pizzas.append('pepperoni')

friends_pizza = pizzas[:]

friends_pizza.append('anchovy')

print(f"\nMy favorite pizzas are:\n")
for pizza in pizzas:
    print(pizza)

print(f"\nMy friend's favorite pizzas are:\n")

for pizza in friends_pizza:
    print(pizza)

