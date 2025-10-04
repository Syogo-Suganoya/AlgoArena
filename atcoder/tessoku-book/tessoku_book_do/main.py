N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
# 符号パターンを4通り試す
for sx in [1, -1]:
    for sy in [1, -1]:
        totalA, totalB = 0, 0
        for i in range(N):
            # このカードを選んだときの寄与度
            contrib = sx * A[i] + sy * B[i]
            if contrib > 0:
                totalA += A[i]
                totalB += B[i]
        # スコア計算
        score = abs(totalA) + abs(totalB)
        ans = max(ans, score)

print(ans)
