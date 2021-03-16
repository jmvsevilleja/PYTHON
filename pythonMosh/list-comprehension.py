print("# List Comprehension")
items = [0, 1]

print([[a, b, c] for a in items for b in items for c in items if True])

print("# Non List Comprehension")
for a in items:
    for b in items:
        for c in items:
            print(a, b, c)

print("# Map / Filter Function")
print(list(map(lambda item: item % 2 == 0, range(0, 11))))  # check even list
print(list(filter(lambda item: item % 2 == 0, range(0, 11))))  # return even list

print("# Map / Filter Function")
print(list(map(lambda item: item * 2, range(0, 11))))  # multiplied
# not multiplied and pass the list value if true which is not 0
print(list(filter(lambda item: item * 2, range(0, 11))))
