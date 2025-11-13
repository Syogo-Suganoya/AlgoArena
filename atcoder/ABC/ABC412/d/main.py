from itertools import permutations

INF = int(1e9)

# 入力
N, M = map(int, input().split())
edges = set()
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # 無向辺としてセットに保存
    edges.add((min(a, b), max(a, b)))

min_ops = INF

# 頂点順列を全探索
for perm in permutations(range(N)):
    # 1サイクルを作る場合
    needed_edges = set()
    for i in range(N):
        u = perm[i]
        v = perm[(i + 1) % N]
        needed_edges.add((min(u, v), max(u, v)))

    # 追加・削除の操作数を計算
    add_count = len(needed_edges - edges)  # 元にない → 追加
    del_count = len(edges - needed_edges)  # 不要な辺 → 削除
    min_ops = min(min_ops, add_count + del_count)

    # N >= 6 の場合は2サイクルに分けるパターンも考慮
    # i = 3 .. N-3 に分割
    if N >= 6:
        for split in range(3, N - 2):
            # 前半サイクル
            first = perm[:split]
            second = perm[split:]
            needed_edges2 = set()
            for seq in [first, second]:
                for j in range(len(seq)):
                    u = seq[j]
                    v = seq[(j + 1) % len(seq)]
                    needed_edges2.add((min(u, v), max(u, v)))

            add_count2 = len(needed_edges2 - edges)
            del_count2 = len(edges - needed_edges2)
            min_ops = min(min_ops, add_count2 + del_count2)

print(min_ops)
