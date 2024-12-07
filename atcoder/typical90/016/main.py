# 入力の取得
N = int(input())
A, B, C = map(int, input().split())

# 答えの初期値を十分大きな値に設定
Answer = float("inf")

# 全探索
for i in range(10000):  # iはAの個数
    for j in range(10000 - i):  # jはBの個数
        # 残りの値を計算
        V = N - i * A - j * B
        R = i + j + (V // C)

        # 条件を満たす場合に答えを更新
        if V % C == 0 and V >= 0 and R <= 9999:
            Answer = min(Answer, R)

# 答えを出力
print(Answer)
