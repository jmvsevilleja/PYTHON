# Programming with Mosh
# https://www.youtube.com/watch?v=f79MRyMsjrQ
import math

# Types of Data
# Number - Integers
print("Is number 1 an Integer?", type(1) is int)
print("Is number 1.5 an Integer?", type(1.5) is int)
# Number - Float/Decimal
print("Is number 1.5 a Decimal/Float?", type(1.5) is float)
print("Is number Maia a Decimal/Float?", type('Maia') is float)
# String - Letter
print("Is Maia a String/Letters?", type('Maia') is str)
# Boolean - Truthiness
print("Is True a Boolean?", type(True) is bool)
print("Is False a Boolean?", type(False) is bool)


mylist = [1, 2, 3]
print("A list: %s" % mylist)

mylist = (1, 2, 3, "test")
print("A list: %d %d %s %s" % mylist)

# %s - String(or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %. < number of digits > f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation(lowercase/uppercase)


print("Hello world!")
2 + 2
x = 1
y = 2
print(id(x))
x, y = 1, 2
print(id(x))
x = y = 1
# ID x mutable address
print(id(x))
x = x + 1
# ID x new immutable (cant change) address
print(id(x))
# Dynamic Variable
# mypy linter will check type annotations
xx: int = 1
xx = 10  # "Str`ing"

# binary
binary = 0b10
print("Binary:", binary)
print("Binary: ", bin(binary))

# hexadecimal
hexa = 0x12c
print("Hex: ", hex(x))

student_count = 1000
rating = 4.99
is_published = False
# Comment
# \" # \' # \\
course_name = "Python\n\"Programming\""
course_description = """
Hello
World"""
print("x:", x)
print("student_count: ", student_count)
print("rating: ", rating)
print("Course description:",  course_description)
print("Length of a variable: ", len(course_name))

print("# Substring")
print(course_name[5])
print(course_name[-5])
print(course_name[1:2])
print(course_name[:3])
print(course_name[:])

print("# Formatted Strings")
first = " jess"
last = "Mark"
full = f"{first} {last} {len(first)}"
print(full)

print("# String Methods")
first = first.title()  # Capital Case
first = first.strip()  # Remove space both,  rstrip right, lstrip left

print("first.replace('s', 'd')", first.replace('s', 'd'))
print("first.find('e')", first.find('e'))  # return index
print("# Expression")
print('"Jess" in first', "Jess" in first)  # return True
print('"Jess" not in first', "Jess" not in first)  # return false

print("# Complex Numbers")
complex_variable = 1 + 2j  # a + bi
print("Complex", complex_variable)
print(10 / 3)  # 3.33 floating poin
print(10 // 3)  # 3 integer division
print(10 % 3)  # 1 modulus remainder
print(10 ** 3)  # exponent 10 power 3

print("# Built-in Functions")
print(round(2.9))
print(abs(-2.9))

print("# Math module")
print(math.ceil(2.2))


print("# Input / Type")
# x = input("x: ")
x = 1
print(type(x))

print("# Casting")
# int() float() bool() str()
y = int(x) + 1
z = float("1.5")
print(y)
print(z)
print(f"x: {x}, y: {y}")

# Falsy
# "" 0 [] None/null
print(bool("False"))  # is True
