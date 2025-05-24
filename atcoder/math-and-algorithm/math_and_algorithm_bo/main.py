N, X, Y = map(int, input().split())

found = False  # 条件を満たす組が見つかったかどうかのフラグ

# a, b, c を 1〜N で全探索
for a in range(1, N + 1):
    for b in range(1, N + 1):
        for c in range(1, N + 1):
            # 残りの1つの数 d を合計 X にするように決定
            d = X - (a + b + c)

            # d が 1〜N の範囲内でなければスキップ
            if not (1 <= d <= N):
                continue

            # 積が Y と一致するかチェック
            if a * b * c * d == Y:
                found = True  # 条件を満たす組を見つけた
                break  # c のループを抜ける
        if found:
            break  # b のループを抜ける
    if found:
        break  # a のループを抜ける

# 最後に答えを出力
print("Yes" if found else "No")
