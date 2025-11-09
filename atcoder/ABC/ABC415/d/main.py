N, M = map(int, input().split())

# (A, B) のペアを読み込み
pairs = [tuple(map(int, input().split())) for _ in range(M)]

# 「1枚のシールをもらうのに必要な空き瓶の純消費量」= (A - B)
# これが小さいほど効率が良い
pairs.sort(key=lambda x: x[0] - x[1])

x = N  # 今持っている瓶入りコーラの本数
ans = 0  # 集めたシールの総数

for A, B in pairs:
    if x < A:
        # 交換に必要な空き瓶本数 A に届かないなら、もう交換できない
        continue

    diff = A - B  # 1回の交換で減る「空き瓶の純数」

    # (x - A) // diff + 1 回の交換が可能
    # 例: x=10, A=6, B=5 なら diff=1 → 10→9→8→7→6 の5回交換できる
    cnt = (x - A) // diff + 1

    # 瓶入りコーラを減らす
    x -= diff * cnt
    # シール枚数を加算
    ans += cnt

print(ans)
