S = input()
K = int(input())
N = len(S)

max_len = 0  # 答えとなる最大長
left = 0  # 尺取り法の左端
dot_count = 0  # 現在のウィンドウ内の '.' の数

# 右端を一つずつ進めていく
for right in range(N):
    if S[right] == ".":
        dot_count += 1  # '.' を見つけたらカウント

    # '.' の数が K を超えてしまったら、左端を動かす
    while dot_count > K:
        if S[left] == ".":
            dot_count -= 1  # 外れる位置が '.' ならカウントを減らす
        left += 1  # ウィンドウを縮める

    # 条件を満たす範囲での最大長を更新
    max_len = max(max_len, right - left + 1)

print(max_len)
