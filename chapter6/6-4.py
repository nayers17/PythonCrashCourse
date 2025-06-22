programming_words = {'list': 'data type that represents a mutable sequence',
                     'tuple': 'immutable sequence data type',
                     'method': 'can be added on to the end of a variable to data',
                     'function': 'temporarily modifies to data',
                     'integer': 'whole number',
                     'float': 'decimal number',
                     'string': 'sequence of text',
                     'if': 'conditial, goes well with for loops',
                     'elif': "feeds off of if statements, goes down to this if doesn't meet if condition",
                     'print': "print function returns value specified",
                     'in': 'looks to see if a value is within a variable',
                     'if-elif-else chain': 'value passes through this chain to see if it meets certain condition, and returns logic if it doesnt meet anything'}

print('These are some programming terms:\n')
for key, value in programming_words.items():
    print(f'{key}: and their corresponding definitions: {value}')
 
print('\nThese are the individual terms:\n')    
for key in programming_words:
    print({key})
    
print('These are the combined terms and definitions with no extra verbiage:\n')
for key, value in programming_words.items():
    print(f'{key}: {value}')

print('\nspace\n')    
sequentials = ['list', 'tuple']
for programming_word in programming_words:
    print(f'Example term: {programming_word.title()}')
    
    if programming_word in sequentials:
        definition = programming_words[programming_word]
        print(f'\t{programming_word.title()}: {definition}')
        
