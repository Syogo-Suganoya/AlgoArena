X, A, D, N = map(int, input().split())

# D = 0 の特別ケース
if D == 0:
    print(abs(X - A))
    exit()

# 正しく範囲を取る
last = A + D * (N - 1)
mi = min(A, last)
ma = max(A, last)

if X <= mi:
    print(mi - X)
elif X >= ma:
    print(X - ma)
else:
    # 範囲内：Dの符号を意識してインデックスを計算
    k = (X - A) // D
    res = min(abs(X - (A + D * k)), abs(X - (A + D * (k + 1))))
    print(res)
