data types:
    - numeric: int, float, bool
    - sequence: str, list tuple, range (ex. range(1000001)), range(0, 30, 3) prints 0,
    - mapping: dict
    - binary: btye, bytearray, memoryview

keyword: 
    for / in = loops through a list
    if = loops through a list based on a condition
    else = conditional statement that runs after if statement when if statement fails
    del invites[0] = deletes value at first index - PERMANENT
    if-elif-else chain:
        age = 12
        if age < 4:    
            print("Your admission cost is $0.")
        elif age < 18:    
            print("Your admission cost is $25.")
        else:    
            print("Your admission cost is $40.")
    

functions: 
    sorted() = temporarily sorts alphabetically
    (sorted(locations, reverse=True)) = sorts in reverse alphabetically temporarily
    len() = shows length of a value
    sum() = sum of values
    round() = rounds float
    min() = smallest 
     in a list
    max() = largest 
     in a list
    sum() = total amount

methods:
    .append() = adds a value to the end of an list indexed last
    .rstrip() = strips the right side of all strings/text
    .strip() = strips white space from each side
    .title()
    .removeprefix() = removes the front text of a string according to what you text you set to remove
    removesuffix('.txt') = removes .txt off end of string
    .pop(0) = removes first indexed value in a list and saves it so you can use it
        - friendwhocantgo = invites.pop(0): assigns value indexed at to "friendwhocantgo"
    .reverse() = permanently reverses list
    .sort() = sorts permanently
    .remove('python') = removes python value from list
    .insert(3, 'Lua') = inserts into index 3 
    .get() = grabs specified value from a dictionary. pass one argument as the key, and a second parameter is optional which is the value that will be returned if false
    .items()
    .keys = useful when you don't need to work with values in a dictionary, just the keys

operators:
    "==" asks if a variable is equal to it's assigned value

logical operators:
    not
    not in

punctuation tokens:
    {} = embedding a variable 
    () = tuple
    [] = list 

escape sequences:
    \n    new line
    \t    tab
    \\    Backslash
    \'    Single quote
    \"    Double quote

misc:
numbers = range(1000001) a range of 1-1,000,000

conditional tests:

text = 'Example'
text.lower() = 'example'
True

number1 = 30
number0 = 20

example: text == 'example' or number0 > 80

--
Test whether an item is in a list: 
'example1' in list and 'example2' in list
'example1' == list and 'example2' == list
--

