# The asterisk in toppings tells python to make a tuple
def make_pizza(*toppings):
    """Prints the list of toppings"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')