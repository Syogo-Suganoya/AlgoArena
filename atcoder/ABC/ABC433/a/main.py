X, Y, Z = map(int, input().split())

for i in range(5000):
    if X + i == (Y + i) * Z:
        print("Yes")
        break
else:
    print("No")
