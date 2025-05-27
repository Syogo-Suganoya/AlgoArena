N = int(input())
A = list(map(int, input().split()))

# 各要素の「現在の位置」を記録するリスト
# 例えば A[i] = x の場合、pos[x] は x の現在位置を保持する
pos = [0] * (N + 1)
for idx, value in enumerate(A):
    pos[value] = idx

# 交換操作の内容を記録するリスト
# 各操作は (i, j) の形式（1-indexed）
operations = []

# 1 から N まで順に正しい位置に配置していく
for i in range(N):
    correct_value = i + 1  # i 番目の位置に欲しい値
    current_value = A[i]  # 今の値

    if current_value == correct_value:
        # すでに正しい値が入っているなら何もしない
        continue

    # correct_value が現在いる位置
    correct_idx = pos[correct_value]

    # correct_value を i 番目に持ってくるために swap
    # スワップ操作を記録（1-indexed にするため +1）
    operations.append((i + 1, correct_idx + 1))

    # スワップ実行
    A[i], A[correct_idx] = A[correct_idx], A[i]

    # 位置情報も更新
    pos[current_value] = correct_idx
    pos[correct_value] = i

print(len(operations))
for op in operations:
    print(op[0], op[1])
