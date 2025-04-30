import bisect

# 入力の読み取り：休憩所の数 n、目標歩数の剰余 m
n, m = map(int, input().split())

# 各休憩所間の距離 a を2周分に拡張してリスト a に格納
a = list(map(int, input().split())) * 2

# r[i] := 始点から i 番目の休憩所までの累積距離の m による剰余
r = [0] * (2 * n + 1)
for i in range(2 * n):
    r[i + 1] = (r[i] + a[i]) % m

# bucket[mod] := 剰余が mod のインデックスの一覧
bucket = [[] for _ in range(m)]
for i in range(2 * n + 1):
    bucket[r[i]].append(i)

ans = 0
# i を終点とした長さ n の区間の中に、始点との距離が m の倍数になるペアを数える
for i in range(n, 2 * n):
    # 現在位置 i での剰余 r[i] と一致する過去の位置を数える
    # i-n < j < i かつ r[j] == r[i] を満たす個数を数える
    # bisect_right により、r[i] の bucket 内で i-1 以下の個数を数える
    ans += bisect.bisect_right(bucket[r[i]], i - 1)
    # i-n 以下のインデックスを除外
    ans -= bisect.bisect_right(bucket[r[i]], i - n)

# 結果を出力
print(ans)
