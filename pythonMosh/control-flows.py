# Programming with Mosh
# https://www.youtube.com/watch?v=f79MRyMsjrQ

print("# Control Flows")

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
# Iterable List
for x in [1, 2, 3]:
    print(x)
# Iterable Range
for number in range(1, 10, 2):
    print("Number", number, number * ".")
# Iterable String
for python in "Python":
    print(python)

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