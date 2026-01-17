# ---------- 前処理 ----------
MAX_M = 10**6

# 素因数の「種類数」を数えるための配列
cnt = [0] * (MAX_M + 1)

# エラトステネスの篩の要領で、
# 各数が何種類の素因数を持つか数える
for p in range(2, MAX_M + 1):
    if cnt[p] == 0:  # p は素数
        for x in range(p, MAX_M + 1, p):
            cnt[x] += 1

# 400 number の候補をすべて列挙
candidates = []
for m in range(1, MAX_M + 1):
    if cnt[m] == 2:
        candidates.append(m * m)

candidates.sort()

# ---------- クエリ処理 ----------
Q = int(input())
for _ in range(Q):
    A = int(input())

    # A 以下の最大の候補を二分探索で探す
    left, right = 0, len(candidates)
    while left < right:
        mid = (left + right) // 2
        if candidates[mid] <= A:
            left = mid + 1
        else:
            right = mid

    # left-1 が条件を満たす最大の位置
    print(candidates[left - 1])
