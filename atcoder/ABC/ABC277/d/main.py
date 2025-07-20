from collections import defaultdict

n, m = map(int, input().split())
a_list = list(map(int, input().split()))

mp = defaultdict(int)
total = 0

# カウントと合計
for a in a_list:
    mp[a] += 1
    total += a

# keyの昇順で (値, 個数) のリストに変換
vec = sorted(mp.items())
k = len(vec)

# 全種類あるなら、全部出せる
if k == m:
    print(0)
    exit()

# ギャップがある位置 p を探す
for i in range(k):
    cur = vec[i][0]
    nxt = vec[(i + 1) % k][0]
    if nxt != (cur + 1) % m:
        p = i
        break

# s配列の準備
s = [0] * k

# 後ろ向きにsを計算
for i in range(k):
    j = (p - i + k) % k
    s[j] = total
    cur_val, cur_cnt = vec[j]

    # 連続しているなら前の値を引き継ぐ
    if vec[(j + 1) % k][0] == (cur_val + 1) % m:
        s[j] = s[(j + 1) % k]

    s[j] -= cur_val * cur_cnt

# 答えは s の最小値
print(min(s))
