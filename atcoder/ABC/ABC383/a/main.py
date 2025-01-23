N = int(input())

T, V = map(int, input().split())
res = V
lastT = T

for _ in range(N - 1):
    T, V = map(int, input().split())
    res = max(res - (T - lastT), 0)
    res += V
    lastT = T

print(res)
