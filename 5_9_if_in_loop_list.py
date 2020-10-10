requested_toppings = ['mushrooms','green peppers','extra cheese']

for loop in requested_toppings:
    if loop == 'green peppers':
        print("sorry, we are out of green peppers right now.")
    else:
        print("Adding " + loop + ".")

print("\nFinished with your pizza")