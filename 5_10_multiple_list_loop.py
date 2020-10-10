available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for loop in requested_toppings:
    if loop in available_toppings:
        print("adding " + loop+ ".")

print("\nFinished making your pizza")