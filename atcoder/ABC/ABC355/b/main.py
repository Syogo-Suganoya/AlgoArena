N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# AとBを辞書にする
d = {}
for a in A:
    d[a] = "A"
for b in B:
    d[b] = "B"

# マージしてソート
merged = sorted(d.items())

# 連続して同じバリューがあればTrueを返す
for i in range(1, len(merged)):
    if merged[i][1] == "A" and merged[i - 1][1] == merged[i][1]:
        print("Yes")
        break
else:
    print("No")
