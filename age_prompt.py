# Use input() to prompt for user input
name = input("Please enter your name: ")

# int() can be used to parse an int. It will throw an exception.
age = int(input("Please enter your age: "))
print("Hello " + name.title() + ". You're " + str(age) + " years old.")
if age >= 18:
    print("It looks like you can vote.")
