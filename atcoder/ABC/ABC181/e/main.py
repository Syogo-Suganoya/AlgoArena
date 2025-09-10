import bisect

N, M = map(int, input().split())
H = list(map(int, input().split()))  # 子どもの身長
W = list(map(int, input().split()))  # 先生の姿（候補）

H.sort()

# 左側（偶数インデックスのペア）の累積和
left = [0] * (N + 1)
for i in range(2, N + 1, 2):
    left[i] = left[i - 2] + (H[i - 1] - H[i - 2])

# 右側（偶数インデックスのペア）の累積和
right = [0] * (N + 1)
for i in range(2, N + 1, 2):
    right[i] = right[i - 2] + (H[N - i + 1] - H[N - i])

ans = float("inf")

for w in W:
    # w を H に挿入したときの位置を求める
    pos = bisect.bisect_left(H, w)

    if pos % 2 == 0:
        # pos が偶数 → w と H[pos] がペアになる
        total = left[pos] + right[N - pos - 1] + abs(H[pos] - w)
    else:
        # pos が奇数 → w と H[pos-1] がペアになる
        total = left[pos - 1] + right[N - pos] + abs(w - H[pos - 1])

    ans = min(ans, total)

print(ans)
