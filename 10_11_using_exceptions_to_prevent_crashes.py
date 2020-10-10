print("Give me two numbers and I will divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

    #NOTE = this program does not yet handle error crashing when division
    # by ZERO takes place. The next code 10_11 does that