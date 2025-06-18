N = int(input())

for i in range(1, 10):
    d, m = divmod(N, i)
    if m == 0 and 1 <= d <= 9:
        print("Yes")
        break
else:
    print("No")
