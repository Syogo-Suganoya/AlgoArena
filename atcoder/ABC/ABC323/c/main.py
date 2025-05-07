import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [input() for _ in range(n)]

# 各人の現在スコアを計算
now_sc = []
for i in range(n):
    score = i + 1  # 基本点
    for j in range(m):
        if s[i][j] == "o":
            score += a[j]
    now_sc.append(score)

mx = max(now_sc)

# 各人ごとに何問解けば最大に追いつくかを二分探索で求める
for i in range(n):
    # まだ解いてない問題を取り出す（得点付き）
    nokori = [a[j] for j in range(m) if s[i][j] == "x"]
    nokori.sort(reverse=True)

    # 累積和
    cumsum = [0]
    for x in nokori:
        cumsum.append(cumsum[-1] + x)

    # 何点足りないか
    need = mx - now_sc[i]

    # 二分探索（何問解けばいいか）
    ans = bisect.bisect_left(cumsum, need)
    print(ans)
