from collections import Counter

K = int(input())
S = input().strip()
T = input().strip()

# 残カード数
rest = [0] + [K] * 9  # rest[0]ダミー
for ch in S[:4] + T[:4]:
    rest[int(ch)] -= 1


def score(hand, extra):
    cnt = Counter(int(c) for c in hand[:4])
    cnt[extra] += 1
    return sum(d * 10 ** cnt[d] for d in range(1, 10))


win = tot = 0
for i in range(1, 10):
    for j in range(1, 10):
        # 取りうる方法数
        ways = rest[i] * (rest[i] - 1) if i == j else rest[i] * rest[j]
        if ways <= 0:  # 在庫なし
            continue
        if score(S, i) > score(T, j):
            win += ways
        tot += ways

print(win / tot)
