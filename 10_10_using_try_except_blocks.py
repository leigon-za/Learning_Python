#for use when you think an error could occur
#you will tell python what to do when a error you think might occur

try:
    print(5/0)
except ZeroDivisionError:
    print("You cant divide by zero")