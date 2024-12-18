N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

mod = 10**9 + 7

res = 1
for i in A:
    res *= sum(i)
    res %= mod

print(res)
