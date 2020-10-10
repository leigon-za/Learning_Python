#prompt / input seems the same. Stores whatever is inserted
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
#message & input runs over and over until ctrl+c entered
while message != 'quit':
    message = input(prompt)
    print(message)