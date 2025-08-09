S = input().strip()
N = len(S)
hugs = 0

# 前半部分をチェック
for i in range(N // 2):
    if S[i] != S[N - 1 - i]:
        hugs += 1

print(hugs)
