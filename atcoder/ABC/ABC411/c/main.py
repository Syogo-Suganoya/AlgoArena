N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * N  # 初期配列
groups = 0  # 初期の1の塊の数

for ai in A:
    idx = ai - 1
    if S[idx] == 0:
        # 0 -> 1 に変わる場合
        left = S[idx - 1] if idx > 0 else 0
        right = S[idx + 1] if idx < N - 1 else 0
        if left == 0 and right == 0:
            groups += 1  # 新しい塊が増える
        elif left == 1 and right == 1:
            groups -= 1  # 両隣の塊が合体して1つに
        # else: 片方だけ1 → 塊の数は変わらない
        S[idx] = 1
    else:
        # 1 -> 0 に変わる場合
        left = S[idx - 1] if idx > 0 else 0
        right = S[idx + 1] if idx < N - 1 else 0
        if left == 0 and right == 0:
            groups -= 1  # 塊が消える
        elif left == 1 and right == 1:
            groups += 1  # 塊が2つに分かれる
        # else: 片方だけ1 → 塊の数は変わらない
        S[idx] = 0
    print(groups)
