from itertools import combinations

# 頂点数 N の木
N = int(input())

# 隣接リストの初期化（辞書を使う）
d = {}
for i in range(1, N + 1):
    d[i] = set()

# 木の辺情報を入力として受け取る
for i in range(N - 1):
    U, V = (int(x) for x in input().split())
    d[U].add(V)
    d[V].add(U)

# 各ノードの「色」を保持する配列
# -1 はまだ訪問していないことを示す
color = [-1] * N

# 根（1番ノード）を赤(=1)に塗る
color[0] = 1

# 現在の塗り分け状態を表すフラグ (0/1)
p = 0

# BFS（幅優先探索）を使って二部グラフに塗り分ける
stack = [1]
next_move = []
while stack:
    for i in stack:
        for j in d[i]:
            # まだ色がついていないノードを反対の色で塗る
            if color[j - 1] == -1:
                color[j - 1] = p
                next_move.append(j)
    # 次の層に進む
    stack, next_move = next_move, []
    p = (p + 1) % 2

# -----------------------------------------------------------------------------
# ここまでで、木を二部グラフとして赤黒に塗り分け終わった
# （color[i] = 0 または 1 で、隣り合うノードは必ず異なる色になる）

# -----------------------------------------------------------------------------
# 次に、すべてのペア (a, b) のうち以下を満たすものを列挙する:
#   - a, b の色が異なる
#   - a と b が直接つながっていない
# これらのペアをゲームの「候補手」とする
res = set()
for i in combinations(range(1, N + 1), 2):
    a, b = i[0], i[1]
    if color[a - 1] != color[b - 1] and b not in d[a] and a not in d[b]:
        if a > b:
            a, b = b, a
        res.add((a, b))

# -----------------------------------------------------------------------------
# 残りのペアの数が奇数なら「First」、
# 偶数なら「Second」が勝つ（Nim的な偶奇判定）
if len(res) % 2 == 1:
    print("First")
else:
    print("Second")
    # 先手が動いた後、相手の手を読み取る
    a, b = (int(x) for x in input().split())
    if a > b:
        a, b = b, a
    res.remove((a, b))

# -----------------------------------------------------------------------------
# ゲームの対話ループ
# 交互にペアを出し合って、ペア集合から削除していく
# (-1, -1) が来たら終了（AtCoder のインタラクティブ仕様）
while True:
    a, b = res.pop()
    print(a, b)  # 自分の手を出す
    a, b = (int(x) for x in input().split())  # 相手の手を受け取る
    if a == -1 and b == -1:
        exit()  # ゲーム終了
    else:
        if a > b:
            a, b = b, a
        res.remove((a, b))
