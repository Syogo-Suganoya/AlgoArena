N, M = map(int, input().split())
A = list(map(int, input().split()))

# 「レ」がある位置を記録
re = [False] * (N + 2)  # 1-based indexing
for a in A:
    re[a] = True

ans = []
i = 1
while i <= N:
    j = i
    # 連結されている限り範囲を広げる
    while re[j]:
        j += 1
    # 連結成分を大きい順に追加
    for k in range(j, i - 1, -1):
        ans.append(k)
    i = j + 1

print(*ans)
