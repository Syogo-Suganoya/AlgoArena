import random

# 入力
N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# 疑似乱数生成器 (C++ の mt19937_64 に相当)
random.seed(58)

T = 100  # 試行回数
for _ in range(T):
    # ランダムに異なる 2 点を選ぶ
    while True:
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        if i != j:
            break

    # 2 点から直線の係数 a*x + b*y + c = 0 を求める
    a = Y[i] - Y[j]
    b = X[j] - X[i]
    c = X[i] * Y[j] - X[j] * Y[i]

    # 選んだ直線上にある点の数を数える
    num = 0
    for k in range(N):
        if a * X[k] + b * Y[k] + c == 0:
            num += 1

    # 過半数を通る直線なら出力して終了
    if num * 2 > N:
        print("Yes")
        print(a, b, c)
        break
else:
    # どの直線も過半数を通らなかった場合
    print("No")
