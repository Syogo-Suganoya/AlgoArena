from sortedcontainers import SortedSet

n, q = map(int, input().split())
a = list(map(int, input().split()))

# bk[i] は 0～n の数 i が A 内で何回出ているかをカウント
bk = [0] * (n + 1)
for val in a:
    if val <= n:  # n より大きい数は mex に影響しないので無視
        bk[val] += 1

# mex 候補を SortedSet で管理（出現していない数だけ）
st = SortedSet(i for i in range(n + 1) if bk[i] == 0)

# Q 回のクエリ処理
for _ in range(q):
    i, x = map(int, input().split())
    i -= 1  # 0-index に調整（Python は 0 始まり）

    # --- 元の値を削除 ---
    if a[i] <= n:
        bk[a[i]] -= 1  # 出現回数を減らす
        if bk[a[i]] == 0:  # これで出現ゼロになったら mex 候補に追加
            st.add(a[i])

    # --- 新しい値を追加 ---
    a[i] = x
    if a[i] <= n:
        if bk[a[i]] == 0:  # 初めて登場する場合は候補から削除
            st.discard(a[i])
        bk[a[i]] += 1  # 出現回数を増やす

    # 現在の mex は候補集合の最小値
    print(st[0])
