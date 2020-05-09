# Programming with Mosh
# https://www.youtube.com/watch?v=f79MRyMsjrQ
import math

print("# Functions")

# Functions and parameters
# Perform a task and return None / value


def greet(first_name, last_name="the Great"):
    print("Hello World")
    print("Welcome", first_name)
    return f"Hi {first_name} {last_name}"


message = greet("Jess")
print(message)
# file = open("jess.txt", "w")
# file.write(message)


def increment(number, by=1):
    return number + by


# keyword argument
print("Increment: ", increment(2, by=1))


def multiply(*numbers):  # arguments - tuples
    product = 1
    for number in numbers:
        print(number)
        # assignment operator
        product *= number
    return product


# Collections of arguments
# list notation [1,2,3,4]
# tuples (1,2,3,4)
print("Multiply: Args: ", multiply(1, 2, 3))


def save_user(**user):  # keyword arguments - dictionary
    print("Dictionary Name: ", user["name"])


# Dictionary Object
save_user(id=1, name="Jess", age=35)

# Scope
# Avoid modify Global variable
greeting = "Hello"


def hello(name):
    global greet
    greet = f"Hi {name}"


# Scope
print(greet)
hello("Jess")
print(greet)


# F5 Run Debug
# Shift F5 Debug to stop
# F10 Line by line Execute
# F11 Step in to a Function
# Shift F11 Stip out into a Function
# F9 Set Breakpoin

print("Start")
print("Multiply: ", multiply(1, 2, 3))

# VSCode Tricks
# Alt Arrow to move code up and down
# Shift Alt Arrow to duplicate
# Comment Ctrl + /


print("Exercise")


def fizz_buzz(input):
    if(input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    if(input % 3 == 0):
        return "Fizz"
    if(input % 5 == 0):
        return "Buzz"
    return input


print(fizz_buzz(15))
