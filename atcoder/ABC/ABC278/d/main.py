N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)  # 1-indexed に合わせるため先頭にダミー0を追加

base = 0  # 一括代入用の基本値
added_index = set(range(1, N + 1))  # 差分が非ゼロかもしれないインデックス

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # type 1: 全体を base に更新し、差分はすべて 0 に
        base = query[1]
        for i in added_index:
            A[i] = 0
        added_index.clear()
    elif query[0] == 2:
        # type 2: 指定の index に value を加算（差分として）
        index, value = query[1], query[2]
        A[index] += value
        added_index.add(index)
    else:
        # type 3: 現在の値（base + 差分）を出力
        index = query[1]
        print(base + A[index])
