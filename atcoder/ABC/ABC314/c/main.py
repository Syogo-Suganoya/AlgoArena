N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

# 色ごとのインデックスを記録
color_positions = [[] for _ in range(M)]
for idx, color in enumerate(C):
    color_positions[color - 1].append(idx)

# 結果の文字列を初期化
result = S.copy()

# 各色ごとに処理
for positions in color_positions:
    if positions:
        # 対応する文字を取得
        chars = [S[pos] for pos in positions]
        # 右に1つ巡回シフト
        chars = [chars[-1]] + chars[:-1]
        # シフト後の文字を配置
        for pos, char in zip(positions, chars, strict=True):
            result[pos] = char

# 結果を出力
print("".join(result))
