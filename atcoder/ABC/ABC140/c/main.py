N = int(input())
B = list(map(int, input().split()))

# 結果用リスト
# 最初と最後はBの端っこがそのままAになる
# 引っ張られるものがないから
l = [B[0]]  # A[0] = B[0]
l.append(B[-1])  # A[N-1] = B[N-2]

# A[1]〜A[N-2] = min(B[i-1], B[i])
for i in range(1, N - 1):
    l.append(min(B[i - 1], B[i]))

print(sum(l))
