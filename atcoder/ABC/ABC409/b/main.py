N = int(input())
A = list(map(int, input().split()))
for x in range(N, -1, -1):
    count = 0
    for a in A:
        if a >= x:
            count += 1
    if count >= x:
        print(x)
        break
