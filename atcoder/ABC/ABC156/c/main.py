N = int(input())
A = list(map(int, input().split()))

# 平均値を求める（四捨五入して整数へ）
avg = round(sum(A) / N)

# すべての |Ai - 平均| の合計を求める
total_diff = 0
for x in A:
    total_diff += abs(x - avg) ** 2

print(total_diff)
