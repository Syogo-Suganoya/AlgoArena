N = int(input())
SP = []
for i in range(N):
    s, p = input().split()
    SP.append([s, int(p), i + 1])

# ソート: S 昇順、P 降順
SP.sort(key=lambda x: (x[0], -x[1]))

# 結果出力
for s, p, idx in SP:
    print(idx)
