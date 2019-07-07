class Dog():
    """A dog"""
    def __init__(self, name, age):
        """Initialize dog"""
        self.name = name
        self.age = age
    
    def sit(self):
        print("Woof woof. " + self.name.title() + " is sitting.")

    def roll_over(self):
        print("Woof woof. " + self.name.title() + " is rolling over.")

my_dog = Dog("anheuser", 7)
my_dog.roll_over()
my_dog.sit()