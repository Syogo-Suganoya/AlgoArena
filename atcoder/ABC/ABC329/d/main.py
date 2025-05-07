N, M = map(int, input().split())
A = list(map(int, input().split()))


l = [0] * (N + 1)
res = 1
for i in A:
    l[i] += 1
    if (l[i] == l[res] and i < res) or l[i] > l[res]:
        res = i
    print(res)
