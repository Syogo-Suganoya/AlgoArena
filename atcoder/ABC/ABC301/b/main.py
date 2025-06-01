N = int(input())
A = list(map(int, input().split()))

res = []
for i in range(N - 1):
    res.append(A[i])
    diff = A[i + 1] - A[i]
    # 1ずつ増減する差分を挿入
    if diff > 0:
        for d in range(1, diff):
            res.append(A[i] + d)
    elif diff < 0:
        for d in range(1, -diff):
            res.append(A[i] - d)

# 最後の要素も忘れずに
res.append(A[-1])

print(*res)
