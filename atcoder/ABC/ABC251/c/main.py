N = int(input())
s = set()
res = -1
point = -1
for i in range(N):
    S, T = input().split()
    if S in s:
        continue
    T = int(T)
    if point < T:
        point = T
        res = i
    s.add(S)
print(res + 1)
