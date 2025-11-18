# 入力
N = int(input())
A = list(map(int, input().split()))

# 全体の和
sumA = sum(A)

# 二乗和
sumSq = sum(a * a for a in A)

# 答え = (sumA^2 - sumSq) / 2
ans = (sumA * sumA - sumSq) // 2

print(ans)
