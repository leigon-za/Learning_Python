class Dog():
    """a simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age  = age

    def sit(self):
        """Simulate a dog sitting in command response"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate dog rolling over in command response"""
        print(self.name.title() + " rolled over!")

my_dog = Dog ('willie',6)

print ("My dog's name is " + my_dog.name.title() + ".")
print ("My dog is " + str(my_dog.age) + "years old")