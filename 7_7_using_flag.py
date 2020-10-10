prompt = "\n Tell me something and I will repeat it back to you: "
prompt += "\n Enter 'quit' to end the program."
#sets program to active
active = True
while active:
    message = input(prompt)
 #if input matches 'quit' then loop stops   
    if message == 'quit':
        active = False
    else:
        print(message)