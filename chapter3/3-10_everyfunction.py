languages = ['python', 'javascript', 'c', 'c++', 'r']

# print function and title method
languages[0].title()
print(languages)

# adding Go to the list
languages.append('go')
print(languages)

# inserting at a specific point in the list 
languages.insert(3, 'Lua')
print(languages)

del languages[3]
print(languages)

# taking off an element and storing it with pop method
popped_languages = languages.pop()
print(popped_languages)

# choosing index with pop
indexed_popped_language = languages.pop(0)
print(indexed_popped_language)

print(languages)

languages.remove('r')
print(languages)

languages.insert(0, 'python')
languages.insert(4, 'r')
print(languages)

# languages.sort()
# print(languages)

# languages.sort(reverse=True)
# print(languages)

print(sorted(languages))

languages.reverse()
print(languages)

print(len(languages))

#intentional
print(languages[-6])

print(languages)