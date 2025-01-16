def digit_sum(x):
    return sum(int(digit) for digit in str(x))


def original_calculator(N, K):
    MOD = 100000
    # nxt[i] = (i + digit_sum(i)) % MOD を事前計算
    nxt = [(i + digit_sum(i)) % MOD for i in range(MOD)]

    # 各数値の訪問時刻を記録する
    time_stamp = [-1] * MOD
    pos = N
    cnt = 0

    # サイクル検出
    while time_stamp[pos] == -1:
        time_stamp[pos] = cnt
        pos = nxt[pos]
        cnt += 1

    cycle_length = cnt - time_stamp[pos]

    # 必要なK回の操作を特定
    if K >= time_stamp[pos]:
        # K = (K - time_stamp[pos]) % cycle_length + time_stamp[pos]
        K = K % cycle_length

    # 最終的な位置を探す
    return time_stamp.index(K)


# 入力例
N, K = map(int, input().split())
print(original_calculator(N, K))
