N, K = map(int, input().split())

# 全通りの組み合わせの数
ans = N**3  # 黒, 白, 灰の3枚カードの組み合わせ

# 条件を満たさない組み合わせを引く
for i in range(1, N + 1):  # 黒カードの値
    for j in range(i - K + 1, i + K):  # 白カードの値の範囲（黒との差がK未満の値）
        if not 1 <= j <= N:  # 1～Nの範囲外はスキップ
            continue

        for k in range(i - K + 1, i + K):  # 灰カードの値の範囲（黒との差がK未満の値）
            if not 1 <= k <= N:  # 1～Nの範囲外はスキップ
                continue

            # 白と灰の差も K 未満の場合、条件を満たさない
            if abs(j - k) < K:
                ans -= 1  # 条件を満たさない組み合わせを引く

# 条件を満たす組み合わせの数を出力
print(ans)
