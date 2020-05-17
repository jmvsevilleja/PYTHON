# x, y, z, n = (int(input()) for _ in range(4))

# print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1)
#        for c in range(0, z+1)])

x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[a, b, c] for a in range(x + 1) for b in range(y + 1)
       for c in range(z + 1) if ((a + b + c) != n)])
