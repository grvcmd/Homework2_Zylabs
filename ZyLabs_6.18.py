n1 = int(input())
n2 = int(input())

if n1 <= n2:
    i = n1
    while i <= n2:
        print(i, end=' ')
        i += 10
    print()
else:
        print("Second integer can't be less than the first.")