N = int(input())
d = {}

for i in range(N):
    A, C = map(int, input().split())
    d[C] = min(d.get(C, 10**9 + 1), A)

print(max(d.values()))
