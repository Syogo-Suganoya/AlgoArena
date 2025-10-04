N = int(input())
s = list(map(int, str(N)))  # 桁のリスト（左が先頭）
L = len(s)

# dp[pos][tight] = (count, sumdig)
# pos: 現在処理中の桁位置（0..L）
# tight: 0=すでに N より小さい状態, 1=まだ N の接頭辞と一致している（上限あり）
# ここでは位置ごとに更新するだけなので 2 要素の配列で持てばよい
dp_count = [[0] * 2 for _ in range(L + 1)]
dp_sum = [[0] * 2 for _ in range(L + 1)]

# 初期: まだ桁を決めていない状態（数 1 個 = 空の数）
dp_count[0][1] = 1
dp_sum[0][1] = 0

for pos in range(L):
    digit_limit = s[pos]
    for tight in (0, 1):
        cnt = dp_count[pos][tight]
        sm = dp_sum[pos][tight]
        if cnt == 0:
            continue
        # 上限は tight==1 のとき digit_limit, そうでなければ 9
        up = digit_limit if tight == 1 else 9
        for d in range(0, up + 1):
            ntight = 1 if (tight == 1 and d == digit_limit) else 0
            # 新状態に追加
            dp_count[pos + 1][ntight] += cnt
            # sumdig の更新：既存の sum（sm）に今回の桁 d が cnt 個分寄与
            dp_sum[pos + 1][ntight] += sm + cnt * d

# 最終的に tight=0 と tight=1 の合計が 0..N の個数・和
total_sum = dp_sum[L][0] + dp_sum[L][1]
print(total_sum)
