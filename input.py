greetings = "Hello"
print(greetings)

name = input("Enter your Name: ")
print(name)

age = input("Enter Age: ")
print(age)
print(type(age))
age = int(age)
print(type(age))
print("%s is %d years old." % (name, age))
