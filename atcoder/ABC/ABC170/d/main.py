MAX = 2100000

N = int(input())
A = list(map(int, input().split()))

v = [0] * MAX
for a in A:
    v[a] += 1

for d in range(1, MAX):
    if v[d] == 0:
        continue
    if v[d] > 1:
        v[d] = 0
    for e in range(d * 2, MAX, d):
        v[e] = 0

res = sum(v)
print(res)
