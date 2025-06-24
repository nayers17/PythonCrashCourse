message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# program runs as long as the user wants by putting program inside a while loop

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program: "

message = ""
while prompt != 'quit':
    message = input(prompt)
    print(message)