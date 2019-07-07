def describe_pet(animal_type, pet_name):
    """Prints info about a pet"""
    print("Your " + animal_type + " is named " + pet_name.title())

# Functions can be invoked like:
describe_pet("dog", "gary")
describe_pet(pet_name = "anheuser", animal_type = "dog")

# Functions can have default values
def describe_pet2(animal_type, pet_name = "freddy"):
    """Prints info about a pet"""
    print("Your " + animal_type + " is named " + pet_name.title())

describe_pet2("horse")
describe_pet2("goat", "danny")

# Return values
def format_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    return first_name.title() + " " + last_name.title()

full_name = format_name("mitch", "gaydash")
print(full_name)

# Passing an arbitrary number of args
def build_pizza(*toppings):
    """Print the pizza w/ toppings"""
    output = ""
    for topping in toppings:
        output += topping + " "
    print("Your pizza has " + output)

build_pizza("sauce", "cheese", "peppers", "onions")