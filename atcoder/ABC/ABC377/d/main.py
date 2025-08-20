N, M = map(int, input().split())
# d[r] = r を右端としたときに許される l の最小値
# 初期値はすべて 1 （つまり最初は l=1 から考えられる）
d = [1] * (M + 1)

# 各区間 [L, R] を処理する
for _ in range(N):
    L, R = map(int, input().split())
    # [l, r] が [L, R] を完全に含まないためには
    # l > L である必要がある（R = r のとき）
    # よって d[R] を L+1 以上に更新する
    d[R] = max(d[R], L + 1)

# 累積的に最小 l を右に伝播させる
# d[r] = max(d[r], d[r-1]) とすることで
# 「r を右に進めると制約が緩むことはない」性質を保つ
for r in range(1, M + 1):
    d[r] = max(d[r], d[r - 1])

# 各 r ごとに可能な (l, r) の組数を足し合わせる
# l の範囲は d[r] <= l <= r なので個数は (r - d[r] + 1)
ans = sum(r - d[r] + 1 for r in range(1, M + 1))

print(ans)
