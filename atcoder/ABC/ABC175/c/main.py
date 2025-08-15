X, K, D = map(int, input().split())

X = abs(X)  # 正負関係なく考える

# まずはできるだけ0に近づく
move = min(K, X // D)
X -= move * D
K -= move

# 残り回数で距離を最小化
if K % 2 == 0:
    print(X)
else:
    print(abs(X - D))
