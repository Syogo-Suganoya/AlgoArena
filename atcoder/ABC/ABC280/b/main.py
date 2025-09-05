N = int(input())
A = list(map(int, input().split()))

# 元の配列を復元する配列
res = [0] * N
res[0] = A[0]  # 最初の要素はそのまま

# 差分を取ることで復元
for i in range(1, N):
    res[i] = A[i] - A[i - 1]

print(*res)
