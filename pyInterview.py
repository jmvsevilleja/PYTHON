# Flow Statements

# Algorithm

print('Fibonacci')  # Fibonacci sequence
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b

print('range')  # range of numbers 0 - 2
for x in range(3):
    print(x)

# Data Types
print('Data Types')
variable = [1, 2, 3, 4, 5]  # List - duplicate values -
print(variable, ' - List')
generator = (num for num in variable)
print(generator, ' - Generator (yeald) - Not in memory')
print([num for num in variable], ' - list() - converted to list - In Memory')

variable = (1, 2, 3, 4, 5)  # Tuple - fixed
print(variable, ' - Tuple')
print(type(variable))
variable = {'id': 1, 'name': 'Jess', 'list': [
    1, 2, 3], 'dict': {1, 2, 3}}  # Dict - any values
for key in variable:
    print(key, ' - Key')
    print(variable[key], ' - Value')
print(type(variable), ' - Dictionary')
# Set - unique, unordered values - searching
variable = {1, 1, '2', (3), 4.5, (1, 2, 3)}
for value in variable:
    print(type(value), ' - Set Variable Type')
    print(value, ' - Value')
print(type(variable), ' - Set - NO mutable items')

# List Comprehension

variable = [1, 2, 3, 4, 5]
squares = [num*num for num in variable]
print("List comprehension: squares: ", squares)
