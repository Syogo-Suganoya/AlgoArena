N = int(input())
S = input()
T = input()

# 文字が異なる箇所の数をカウント
count = 0
for i in range(N):
    if S[i] != T[i]:
        count += 1

print(count)
