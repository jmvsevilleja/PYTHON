from pprint import pprint
from sys import getsizeof
print("# List")

name = "Jess Mark"
print("string to list:", name.split())

print('# Lists')  # list of values - w/ key
letters = ["a", "b", "c"]
zeros = [0] * 5
print(letters)
print(zeros)
print(letters + zeros)
print(list(range(5)))
print(list("Hello World"))
print("zeroes: ", len(zeros))


print("# Access List")
print("letters[1]: ", letters[1])
numbers = list(range(21))  # iterable
print("even numbers", numbers[::2])
print("reverse order", numbers[::-1])

print("# Unpacking List")
numbers = [1, 2, 3, 4, 5, 6]
one, two, three, *other, last = numbers
print("Unpacking List: ", one, two, three, other, last)

print("looping over List")
for value in letters:
    print(f"Value: {value}")

print("looping over List via enumerate")
for key, value in enumerate(letters):
    print(f"Key: {key} Value: {value}")

print("Adding Removing")
letters.append("d")
letters.insert(0, "x")
print(letters)
letters.pop()  # remove last
letters.remove("a")  # remove first
print(letters)
del letters[0: 2]  # remove range
print(letters)
letters.clear()
print(letters)

print("Finding List")  # finding in list
letters = ["a", "b", "c", "d", "d"]
print("Find d: ", "d" in letters)  # True
print("Count d: ", letters.count("d"))  # 2

print("Sorting List")  # sorting basics
numbers = [3, 41, 2, 9, 6]
numbers.sort()
print("Sort: ", numbers)
print("Sorted: ", sorted(numbers, reverse=True))  # will not modify numbers
print(numbers)

print("Sorting 2D List")  # sorting with key
items = [  # list of tuples
    ("a", 2),
    ("b", 3),
    ("c", 1),
]
# function = LAMBDA parameters: expression
items.sort(key=lambda item: item[1])
print(items)

print("Map List Function")  # iterate each list
prices = list(map(lambda item: item[1], items))
print(prices)

print("Filter Function")  # filter each list
prices = list(filter(lambda item: item[1] > 1, items))
print(prices)

print("# List Comprehension")  # shortcut to map and filter
prices = [item[1] for item in items]  # Show key 2 of a list of tuples
print(prices)
prices = [item for item in items if item[1] > 1]  # Filter each list
print(prices)

# [EXPRESSION for item in items]
print([x for x in numbers])  # Show each list
print([x*x for x in numbers if x < 10])  # Square each list and filter

print("# Zip Function")  # generate list of tuples
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print("ZIP", list(zip("a,b,c", list1, list2)))


print("# Stack")  # LIFO last in last out
lists = []
lists.append(1)
print(lists)
lists.pop()

if not lists:
    print("Empty list")

print("# Queue")  # LIFO last in last out
# 	From collections import deque
# 	queue = deque([])
# 	queue.append()
#   queue.popleft()

print("# Tuple")  # sequence of object that is read only - w/o key
print(type((5,)))
point = (1, 2) * 2
print(point)
string = tuple("Hello World")  # string to tuple
print(string)

print("looping over Tuple")
for value in point:
    print(f"Value: {value}")

print("looping over Tuple via enumerate")
for key, value in enumerate(point):
    print(f"Key: {key} Value: {value}")

for key in point:
    print(f"Key: {key} Value: {point[key]}")  # using point

print("# Tuple Comprehension")  # Gernerate values
tuples = (x*2 for x in range(1000))  # in each iteration
lists = [x*2 for x in range(1000)]
print("Tuples: ", tuples)
# Tuples:  <generator object <genexpr> at 0x0000017A28B5E900>
print("Generator: ", getsizeof(tuples))  # no Len - disadv
print("List: ", getsizeof(lists))  # high memory - disadv
print("List Len: ", len(lists))  # adv


print("# SWAP Variables")
x = 10
y = 11
x, y = y, x
print(x, y)

print("# Arrays")  # for large sequence of numbers, can be different types
numbers = [1, 2, 3]


# https://realpython.com/python-sets/
print("# Sets")  # collection without duplicates - w/o key
first = [1, 1, 2, 3, 4]
first = set(first)  # cast - iterable - set declaration
# print(first[0])  sets do not support indexing, slicing, or other sequence-like behavior.
print("Uniques: ", first)
second = {1, 5, 6}  # Set declaration - without key
second.add(5)  # set methods
print(second)
second.remove(5)
print('second', second)
print(len(second))


# advantage
print("Merge:", first | second)
print("Intersection: ", first & second)

print("# Sets Comprehension")
# [expression for item in items]
sets = {x*2 for x in range(5)}
print("Sets: ", sets)

print("looping over Sets")
for value in first | second:
    print(f"Value: {value}")

print("looping over Sets via enumerate")
for key, value in enumerate(first | second):
    print(f"Key: {key} Value: {value}")

# sets_coords = {{"x": 1}}  # sets of dictionaries
# Sets of Dictionaries is not allowed coz Dictionaries are mutable

print("# Dictionaries")  # Collection of key value pairs - w/ key

point = {"x": 1, "y": 2}  # dict declaration
print(point["x"])

points = dict(x=11, y=12, z=13)  # dict declaration
print(points["z"])

for key in points:  # key
    print("key: %s value: %s" % (key, points[key]))  # using points

for value in points:  # value
    print(f"value:{value} ")  # using points

for key, value in points.items():  # using items
    print('key:', key, '', 'value:', value)

print(point.get("z", 0))
del points['z']
print("items: ", points.items())  # dict_items([('x', 11), ('y', 12)])
print("values: ", points.values())  # dict_values([11, 12])
print("keys: ", points.keys())  # dict_keys(['x', 'y'])

print("# Dictionary to List")
print(list(points.items()))  # [('Gabby', 8), ('Maelle', 5)]
print(list(points.keys()))  # ['Gabby', 'Maelle']
print(list(points.values()))  # [8, 5]

list_coords = [{"x": 1}, {"y": 1}]  # list of dictionaries
print("List of Dictionaries: ", list_coords[0]['x'])

coords = {  # dictionary of dictionaries
    1: {"x": 1, "y": 2, "z": 3},
    2: {"x": 4, "y": 5, "z": 6},
    3: {"x": 3, "y": 4, "z": 5},
}
coords[4] = {"x": 7, "y": 8, "z": 9}  # insert

print("Coords", coords)  # {1: {'x': 1, 'y': 2, 'z': 3}, 2: {'
print("Coords", coords[4]["z"])
print("Values", coords.values())  # list of dicts [{'x': 1, 'y': 2, 'z': 3}, {'
sorts = sorted(coords.values(), key=lambda pnt: pnt["x"])
print("Sorted Dict ", sorts)

print("# Dictionary Comprehension")
# [expression for item in items]
dics = {x: x*2 for x in range(5)}
print("Dictionary: ", dics)


print("# Unpacking")  # return iterables
numbers = [*numbers, 1, 2, 3]
print("Unpacked list: ", numbers)
print("Unpacked string: ", *"Hello")
first = {"x": 1}
second = {"x": 2, "y": 2}
combined = {**first, **second, "z": 3}
print("Unpacked dicts: ", combined)


print("# Exercise")
sentence = "This is a common interview common"

word_freq = {}

for word in sentence.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
pprint(word_freq, width=1)  # pprint dictionary
print(word_freq.items())
highest = sorted(word_freq.items(), key=lambda word: word[1], reverse=True)[0]
print("Highest word count: ", highest)

char_freq = {}

for char in list(sentence):
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

highest = sorted(char_freq.items(), key=lambda char: char[1], reverse=True)[:5]
print("Highest character count: ", highest)
