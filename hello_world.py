# Chapter 1
message = "Hello Pyton World!"
print(message)

# Chapter 2 - Variables
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
