from sortedcontainers import SortedList

N, K = map(int, input().split())
P = list(map(int, input().split()))

# 数値iのPにおける位置を保存
pos = [0] * (N + 1)
for i in range(N):
    pos[P[i]] = i

# 初期のK個分の位置を追加
s = SortedList()
for i in range(1, K + 1):
    s.add(pos[i])

ans = s[-1] - s[0]

# スライドしていく
for i in range(K + 1, N + 1):
    s.remove(pos[i - K])
    s.add(pos[i])
    ans = min(ans, s[-1] - s[0])

print(ans)
