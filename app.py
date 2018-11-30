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

# Substring
print(course_name[5])
print(course_name[-5])
print(course_name[1:2])
print(course_name[:3])
print(course_name[:])

# Formatted Strings
first = " jedd"
last = "Mark"
full = f"{first} {last} {len(first)}"
print(full)

# String Methods
first = first.title()
first = first.strip()
print(first.replace('d', 's'))
print(first.find('e'))
# Expression
print("Jedd" in first)
print("Jess" not in first)

# Complex Numbers
x = 1 + 2j  # a + bi
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
print(round(2.9))
print(abs(-2.9))

# Math

print(math.ceil(2.2))

# Input / Type
x = input("x: ")
print(type(x))

# Cast
# int() float() bool() str()
y = int(x) + 1
print(y)
print(f"x: {x}, y: {y}")
