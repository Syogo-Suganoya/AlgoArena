from collections import defaultdict, deque

N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

# 文字列をリストに変換
result = list(S)

# 色ごとのインデックスを取得
color_indices = defaultdict(list)
for i, color in enumerate(C):
    color_indices[color].append(i)

# 各色ごとに右巡回シフト
for indices in color_indices.values():
    if len(indices) > 1:  # 要素が1つならシフト不要
        # シフト前の文字を取得
        temp = [result[i] for i in indices]
        # dequeを用いて右に1シフト
        temp = deque(temp)
        temp.rotate(1)
        # シフト後の文字を元の位置に戻す
        for i, char in zip(indices, temp, strict=False):
            result[i] = char

result = "".join(result)
print(result)
