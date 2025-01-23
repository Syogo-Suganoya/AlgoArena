S = list(input())

res = 0
for i, val in enumerate("atcoder"):
    while S[i] != val:
        a = S.index(val)
        S[a], S[a - 1] = S[a - 1], S[a]
        res += 1

print(res)
