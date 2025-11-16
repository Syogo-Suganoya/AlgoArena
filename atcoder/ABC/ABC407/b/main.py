X, Y = map(int, input().split())

count = 0

# サイコロ2個の出目を全探索
for a in range(1, 7):
    for b in range(1, 7):
        if a + b >= X or abs(a - b) >= Y:
            count += 1

# 確率を計算
probability = count / 36

print(f"{probability:.9f}")
