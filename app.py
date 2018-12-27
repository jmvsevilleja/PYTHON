import math

print("Hello world!")
2 + 2
x = 1
unit_price = 3

student_count = 1000
rating = 4.99
is_published = False
# Comment
# \" # \' # \\
course_name = "Python\n\"Programming\""
course_description = """
Hello
World
"""

print(student_count)
print(rating)
print(course_description)
print(len(course_name))

print("# Substring")
print(course_name[5])
print(course_name[-5])
print(course_name[1:2])
print(course_name[:3])
print(course_name[:])

print("# Formatted Strings")
first = " jedd"
last = "Mark"
full = f"{first} {last} {len(first)}"
print(full)

print("# String Methods")
first = first.title()
first = first.strip()
print(first.replace('d', 's'))
print(first.find('e'))
print("# Expression")
print("Jedd" in first)
print("Jess" not in first)

print("# Complex Numbers")
x = 1 + 2j  # a + bi
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
print(round(2.9))
print(abs(-2.9))

print("# Math")
print(math.ceil(2.2))

print("# Input / Type")
# x = input("x: ")
x = 1
print(type(x))

print("# Cast")
# int() float() bool() str()
y = int(x) + 1
z = float("1.5")
print(y)
print(z)
print(f"x: {x}, y: {y}")

print(bool("False"))

print("# Fundamentals Programming")

print("# Comparison")
print(10 > 3)
print(10 == "10")
print("bag" > "apple")
print("bag" > "BAG")
print(ord("a"))
print(ord("b"))

print("# Conditional")
age = 18
if age > 18:
    message = f"{age} is greater than 18"
elif age < 18:
    message = f"{age} is less than 18"
else:
    massage = f"{age} is equals 18"
print(massage)

print("# Ternary Operator")
message = f"{age} is eligible" if age >= 18 else f"{age} is not Eligible"
print(message)

print("# Logical Operator")
# and or not
high_income = False
good_credit = True
student = False

# Short circuit operator, if high_income is false never called 2nd argument
if (high_income and good_credit) and not student:
    print("Eligible for Loan")
else:
    print("Not Eligible Loan")

# Chain comparison
# age should between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not Eligible")


print("# Loops")
# Iterable
for x in [1, 2, 3]:
    print(x)

for x in "Python":
    print(x)

for number in range(1, 10, 2):
    print("Number", number, number * ".")

successful = False
for number in range(1, 4):
    print("Attempt", number)
    if successful:
        print("Successful")
        break
# for else if it doesn't break
else:
    print("Attemted 3 times and failed")

# Nested Loops
for x in range(2):
    for y in range(2):
        print(f"{x}, {y}")

# While Loop
number = 100
while number > 0:
    print(number)
    # assignment operator
    number //= 2

# Command
command = ""
while command.lower() != "quit":
    command = "quit"  # input(">")
    print("ECHO", command)

# Infinite Loop
while True:
    command = "quit"  # input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

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


def multiply(*numbers):
    product = 1
    for number in numbers:
        print(number)
        # assignment operator
        product *= number
        return product


# Collections of arguments
# list notation [1,2,3,4]
# tuples (1,2,3,4)
print("Multiply: ", multiply(1, 2, 3))


def save_user(**user):
    print("Name: ", user["name"])


# Dictionary Object
save_user(id=1, name="Jess", age=35)

# Scope
# Avoid modify Global variable
greet = "Hello"


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
print("Start")
print("Multiply: ", multiply(1, 2, 3))
print("Multiply: ", multiply(1, 2, 3))

# VSCode Tricks
# Alt Arrow to move code up and down
# Shift Alt Arrow to duplicate
