T = int(input())

results = []
for _ in range(T):
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    # 1. 各要素 A[i] を 2W の余りでグループ化 (O(N))
    # これにより、N が大きくても計算量を 2W に抑えられる
    mod_sum = [0] * (2 * W)
    for i in range(N):
        mod_sum[i % (2 * W)] += A[i]

    # 2. 初期状態 (x=0) の合計を計算
    # 条件 (i + 0) % 2W < W なので、インデックス 0 から W-1 まで
    current_sum = sum(mod_sum[:W])
    min_sum = current_sum

    # 3. スライディングウィンドウで x を 1 から 2W-1 までずらす (O(W))
    # x が 1 増えるごとに、条件を満たすインデックスの範囲が「左」に1つずれる
    for x in range(1, 2 * W):
        # 外れる要素: インデックス (W - x)
        # 加わる要素: インデックス (2*W - x)
        # ※負のインデックスを防ぐため、実際には mod 2W で計算
        remove_idx = (W - x) % (2 * W)
        add_idx = (2 * W - x) % (2 * W)

        current_sum = current_sum - mod_sum[remove_idx] + mod_sum[add_idx]

        if current_sum < min_sum:
            min_sum = current_sum

    results.append(str(min_sum))

print("\n".join(results) + "\n")
