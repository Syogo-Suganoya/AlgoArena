N = int(input())
P = list(map(int, input().split()))

now = N
res = 0
while now != 1:
    now = P[now - 2]
    res += 1
print(res)
