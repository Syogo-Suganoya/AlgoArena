N = int(input())
P = list(map(int, input().split()))

# 0-indexed にする
P = [p - 1 for p in P]

# ans[i] = i が属するサイクルの長さ
ans = [0] * N

for i in range(N):
    if ans[i] != 0:
        continue

    # サイクル検出
    p = i
    count = 0
    while True:
        count += 1
        p = P[p]
        if p == i:
            break

    # サイクルに属する全頂点にサイクル長を記録
    p = i
    while True:
        ans[p] = count
        p = P[p]
        if p == i:
            break

# (総和 - N) // 2 を出力
print((sum(ans) - N) // 2)
