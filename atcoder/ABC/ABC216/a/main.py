X, Y = map(int, input().split("."))
if Y <= 2:
    print(f"{X}-")
elif Y <= 6:
    print(f"{X}")
else:
    print(f"{X}+")
