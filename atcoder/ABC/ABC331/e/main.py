N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# NGを集合で管理する（検索を速くするため）
NG = [set() for _ in range(N)]
for _ in range(L):
    c, d = map(int, input().split())
    NG[c - 1].add(d - 1)

# サイド料理を値段でソートしておく（大きい順）
B_sorted = sorted([(b, j) for j, b in enumerate(B)], reverse=True)

ans = 0
# 各メイン料理について、一番高いサイドから順に探す
for i in range(N):
    for b, j in B_sorted:
        if j not in NG[i]:  # NGでなければOK
            ans = max(ans, A[i] + b)
            break  # そのメインでベストなサイドが見つかったので次へ

print(ans)
