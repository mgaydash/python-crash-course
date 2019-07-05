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
