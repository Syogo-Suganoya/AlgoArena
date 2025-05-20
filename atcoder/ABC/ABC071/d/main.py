MOD = 10**9 + 7

N = int(input())
S1 = input()
S2 = input()

i = 0
res = 1

while i < N:
    if S1[i] == S2[i]:
        # 縦ドミノ
        if i == 0:
            res *= 3
        else:
            if S1[i - 1] == S2[i - 1]:
                res *= 2
            else:
                res *= 1
        i += 1
    else:
        # 横ドミノ
        if i == 0:
            res *= 6
        else:
            if S1[i - 1] == S2[i - 1]:
                res *= 2
            else:
                res *= 3
        i += 2
    res %= MOD

print(res)
