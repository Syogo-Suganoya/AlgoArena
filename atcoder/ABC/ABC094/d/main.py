N = int(input())
A = list(map(int, input().split()))

A.sort()
x = A[-1]  # 最大値

# 二項係数が最大になるのは y = A[i] を x/2 に最も近い値として選ぶとき
y = min(A[:-1], key=lambda a: abs(2 * a - x))

print(x, y)
