N = int(input())
A = list(map(int, input().split()))
A = [0] + A

# 累積和を作る
cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + A[i]

# 区間ごとの和を出力
for i in range(1, N):
    row = []
    for j in range(i, N):
        # A[i]からA[j]までの和
        row.append(str(cum[j + 1] - cum[i]))
    print(" ".join(row))
