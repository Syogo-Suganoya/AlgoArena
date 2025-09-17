s = input().strip()
t = input().strip()
n = len(s)

# もし t の中に s に存在しない文字があれば -1
if set(t) - set(s):
    print(-1)
    exit()

# -------------------------
# nex[i][c] : s[i:] の中で最初に文字 c が出てくる位置
# i = n のときは「存在しない」ことを表す n
# -------------------------
nex = [[n] * 26 for _ in range(n + 1)]

# 後ろから埋めていく
for i in range(n - 1, -1, -1):
    nex[i] = nex[i + 1][:]  # コピー
    nex[i][ord(s[i]) - ord("a")] = i

# 探索開始
pos = 0  # 今 s のどこにいるか
ans = 0  # t を部分列にするために必要な長さ

for ch in t:
    idx = ord(ch) - ord("a")
    if nex[pos][idx] < n:
        # pos 以降で見つかった
        ans += nex[pos][idx] - pos + 1
        pos = nex[pos][idx] + 1
        if pos == n:  # s を1周し終えたら先頭に戻る
            pos = 0
    else:
        # pos 以降にはないので、次の s の頭から探す
        ans += n - pos  # 残りを全部消費
        ans += nex[0][idx] + 1
        pos = nex[0][idx] + 1
        if pos == n:
            pos = 0

print(ans)
