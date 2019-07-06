# Chapter 1 - Hello World
print("Chapter 1")
print("#########################################")

message = "Hello Pyton World!"
print(message)

# Chapter 2 - Variables
print("\nChapter 2")
print("#########################################")

message = "Hello Pyton Crash Course World!"
print(message)

# Variables should be named with lower-case letters and underscores
# No camel case here!
naming_message = "Hello there, snake case ;-)"
print(naming_message)

# Chapter 2 - Strings
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "joseph"
last_name = "stalin"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# /n is a newline
# /t is a tab

# rstrip() and lstrip() strip whitespace from the right an left of strings
favorite_language = "python "
print(favorite_language + "<")
print(favorite_language.rstrip() + "<")

favorite_language = " python "
print(">" + favorite_language + "<")
print(">" + favorite_language.rstrip().lstrip() + "<")

# Chapter 2 - Numbers

# Math
print(3 + 3)
print(3 - 3)
print(3 * 3)
print(3 ** 3) # Exponent
print (4 % 3) # Mod

# Floats
# Note decimal places in output
print(0.2 * 0.2)

# Printing numbers w/ Strings
# print("Hello " + 77) << Error
print("Hello " + str(77))

# Chapter 3 - Lists
print("\nChapter 3")
print("#########################################")

lyrics = ["can", "I", "get", "another", "amen"]
print(lyrics)
print(lyrics[1]) # Indices start at 0

# Can lists have mixed contents? << Yes
mixed_list = ["string", 7, {"name": "Joe"}]
print(mixed_list)
print(mixed_list[2]["name"])

# Modifying list contents
motorcycles = ["yamaha", "honda", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)
motorcycles.append("yamaha")
print(motorcycles)
motorcycles.insert(1, "harley")
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# A list is also a stack
motorcycle = motorcycles.pop()
print("Popped motorcycle: " + motorcycle)
print(motorcycles)

# pop() can be used like del too (More OOP)
motorcycles.pop(1)
print(motorcycles)

# del however can be used to remove ranges
motorcycles.extend(["harley", "yamaha", "honda"])
print(motorcycles)
del motorcycles[2:]
print(motorcycles)

# Remove from list by value
motorcycles.extend(["harley", "yamaha", "honda"])
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

# Organizing a list
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

# sort() is a mutator
cars.sort()
print(cars)

# The sort can be reversed
cars.sort(reverse=True)
print(cars)

# sorted() can be used to preserve the original order
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
print(sorted(cars))
print(cars)

# Lists can be reversed
print(cars)
cars.reverse()
print(cars)

# Use len() to find the length of a list
print(len(cars))

# We have the following list:
test_list = ["one", "two", "three", "four", "five"]
# Elements can be addressed as follows:
#       -->  0      1      2        3       4
#           -5     -4     -3       -2      -1   <--
print(test_list[4])
print(test_list[-1])
print(test_list[-2])

# Chapter 4 - Lists and Loops
print("\nChapter 4")
print("#########################################")

# Loop contents are determined by indentation

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

# Doing more in a loop
for magician in magicians:
    print("Damn, " + magician.title() + ", that was a neat trick")
    print("Wow!")

# range() in for loop << probably not useful ??
for num in range(1, 5):
    print(num)

# range() to create a list
print(list(range(1, 5)))

# Start w/2, add 2, continue until <= 11
print(list(range(2, 11, 2)))

# List of first 10 squares
squares = []
for num in range(1, 11):
    squares.append(num**2)
print(squares)

# List comprehensions
squares = [num**2 + 1 for num in range(1, 11)]
print(squares)

# Working with part of a list

# List slicing
# Second index is exclusive
players = ["tom", "lisa", "kyle", "megan", "erin"]
print(players)
print(players[1:3])

# Both indices are optional
print(players)
print(players[2:])
print(players[:3])

# Slices can be looped
for player in players[:3]:
    print("Hey, " + player.title())

# By omitting the start and end index, a list can be copied
my_foods = ["pizza", "burger", "fries", "hotdog"]
print("My foods are:")
print(my_foods)

friend_foods = my_foods[:]
friend_foods.append("sushi")
friend_foods.remove("pizza")
print("My friend's foods are:")
print(friend_foods)

# Tuples - Immutable lists

dimensions = (100, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[1] = 200 << Error

# Tuples can be iterated just like lists

# Tuples can be reassigned
dimensions = (200, 100)
print(dimensions)

# Styling
# Indent using 4 spaces
# Generally speaking, lines should be no more than 80 characters long

# Chapter 4 - Conditional Statements
print("\nChapter 5")
print("#########################################")

# String comparison
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

for car in cars:
    if "bmw" == car.lower():
        print(car.upper())
    else:
        print(car)

# Numeric comparison
age = 21
print(age == 18)
print(age > 18)
print(age < 18)
print(age > 18 and age < 30)
print(age > 30 or age < 25)

# Checking if a value is (not) in a list
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
print("ford" in cars)
if "ford" not in cars:
    cars.append("ford")
print(cars)
print("ford" in cars)

# If Statements and the if-elif-else chain
age = 19
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
elif age == 18:
    print("Dang, daddy, you 18!")
else:
    print("Sorry. You are not old enough to vote.")

# Checking if lists are empty
requested_toppings = ["onion", "peppers"]
if requested_toppings:
    for topping in requested_toppings:
        print("You've requested " + topping + ".")
else:
    print("There are no pizza toppings.")

# Multiple list example
available_toppings = ["cheese", "pepperoni", "onion", "peppers", "mushrooms"]
requested_toppings = ["pepperoni", "cheese", "french fries"]

for topping in requested_toppings:
    if topping in available_toppings:
        print(topping + " added to pizza.")
    else:
        print(topping + " is not available.")
print("Your pizza is ready!")