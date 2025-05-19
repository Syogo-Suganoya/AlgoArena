S = list(map(int, input().split()))
K = int(input())

sa = max(S)
S.remove(sa)

res = sum(S) + (sa * (2**K))
print(res)
