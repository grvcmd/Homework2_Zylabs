# (a * x) + (b * y) = c
a = int(input())
b = int(input())
c = int(input())

# (d * x) + (e * y) = f
d = int(input())
e = int(input())
f = int(input())

satisfied = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            satisfied = True

if satisfied != True:
    print('No solution')