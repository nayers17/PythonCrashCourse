# bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# print(bicycles[0].title())

# print(bicycles[1])
# print(bicycles[3])
# print(bicycles[-1])

# message = f"I purchased a bike and the brand is {bicycles[0].title()}"

# print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles[0])
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles.insert(2, 'example')
print(motorcycles)

del motorcycles[2]
print(motorcycles)