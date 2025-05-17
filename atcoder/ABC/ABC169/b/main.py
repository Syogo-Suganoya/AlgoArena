N = int(input())
A = list(map(int, input().split()))
res = 1
if 0 in A:
    print(0)
    exit()
for a in A:
    res *= a
    if res > 10**18:
        res = -1
        break
print(res)
