from itertools import product

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

res = 0  # 最大値を記録

# 各人が C を選ぶか D を選ぶかの全パターン（2^K 通り）を試す
for pattern in product([0, 1], repeat=K):
    placed = set()  # この組み合わせで選ばれた皿をセットで記録

    for i in range(K):
        c, d = CD[i]
        # pattern[i] が 0 なら c を、1 なら d を選ぶ
        chosen = c if pattern[i] == 0 else d
        placed.add(chosen)

    # 条件 AB を満たすものを数える
    tmp = 0
    for a, b in AB:
        if a in placed and b in placed:
            tmp += 1

    # 最大値を更新
    res = max(res, tmp)

print(res)
