import bisect

H, W, N = map(int, input().split())

l = []
la = []
lb = []

# 入力とA, B一覧の収集
for _ in range(N):
    A, B = map(int, input().split())
    l.append((A, B))
    la.append(A)
    lb.append(B)

# A, B に登場した値を重複なし昇順に
da = sorted(set(la))
db = sorted(set(lb))

# 各(A, B)に対して、da/db内でのインデックスを求める（1-indexed）
for A, B in l:
    ra = bisect.bisect_left(da, A) + 1
    rb = bisect.bisect_left(db, B) + 1
    print(ra, rb)
