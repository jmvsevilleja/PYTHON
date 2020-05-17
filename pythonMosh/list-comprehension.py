print("# List Comprehension")
items = [0, 1]

print([[a, b, c] for a in items for b in items for c in items if True])

print("# Non List Comprehension")
for a in items:
    for b in items:
        for c in items:
            print(a, b, c)
