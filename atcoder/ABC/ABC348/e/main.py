import sys

sys.setrecursionlimit(10**7)

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

c = list(map(int, input().split()))

subtree_sum_c = [0] * n
subtree_sum_dist = [0] * n

# --- iterative DFS で部分木計算 ---
stack = [(0, -1, 0)]  # (node, parent, state) state=0: 行きがけ, 1: 帰りがけ
order = []
while stack:
    v, par, state = stack.pop()
    if state == 0:
        stack.append((v, par, 1))
        for to in tree[v]:
            if to == par:
                continue
            stack.append((to, v, 0))
    else:
        # 帰りがけに子の結果を集約
        for to in tree[v]:
            if to == par:
                continue
            subtree_sum_c[v] += subtree_sum_c[to]
            subtree_sum_dist[v] += subtree_sum_dist[to]
        subtree_sum_dist[v] += subtree_sum_c[v]
        subtree_sum_c[v] += c[v]

f = [0] * n

# --- iterative rerooting ---
stack = [(0, -1, 0, 0)]  # (v, parent, par_sum_c, par_sum_dist)
while stack:
    v, par, pc, pd = stack.pop()
    f[v] = subtree_sum_dist[v] + pd
    for to in tree[v]:
        if to == par:
            continue
        nc = pc + subtree_sum_c[v] - subtree_sum_c[to]
        nd = pd + subtree_sum_dist[v] - subtree_sum_dist[to] - subtree_sum_c[to] + nc
        stack.append((to, v, nc, nd))

print(min(f))
