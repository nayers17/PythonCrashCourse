locations = ['miami', 'washington d.c.', 'seattle', 'new nork city', 'silicon valley']
print(locations)

# using sorted() function to temporarily modify the list order alphabetically
print(sorted(locations))

# reverse alphabetical without changing the mutable variable location
print(sorted(locations, reverse=True))

print(locations)


# reversing the list permanently on the mutable object
locations.reverse()
print(locations)

# adjusting the order to be alphabetical permanently on mutable object assigned to variable "locations"
locations.sort()
print(locations)

# adjusting the object to permanently change to reverse alphabetical order 
locations.sort(reverse=True)
print(locations)

