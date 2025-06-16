# bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# print(bicycles[0].title())

# print(bicycles[1])
# print(bicycles[3])
# print(bicycles[-1])

# message = f"I purchased a bike and the brand is {bicycles[0].title()}"

# print(message)

## creating a list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles[0])
# print(motorcycles)


## adding a ducati to the end of the list with append method
motorcycles.append('ducati')
print(motorcycles)


## reassigning an empty list value to motorcycles to practice appending to a list
motorcycles = []
print(motorcycles)


motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)


## practicing with insert vs. append
motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles.insert(2, 'example')
print(motorcycles)

## practicing the delete function, deleting the element at index 2
del motorcycles[2]
print(motorcycles)

## practicing pop: taking the last element from the last, removing it from the list,
# and assigning the variable "popped_motorcycle" the value of the removed element "suzuki"
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

# checking to see if it actually removed it from the list assigned to motorcycles (yes, it did)
print(motorcycles)

## real world example of using pop
print(f"The last motorcycle I bought was a {popped_motorcycle.title()}.")

first_motorcycle_purchase = motorcycles.pop(0)
print(first_motorcycle_purchase)

print(f"The first motorcycle I ever purchased was a {first_motorcycle_purchase.title()}.")

motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

# practicing with .remove() method: if you don't know the index of the element, but you
# know the name of the element, then you should use the .remove() method 

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

## removing an element with a variable that holds a value of the element we want to remove
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nThe {too_expensive.title()} is too expensive for me to insure and maintain, so I sold it.")

