import sys

input = sys.stdin.readline

# 入力 N, K を取得
N, K = map(int, input().split())

# 木の隣接リスト T を作成（0-indexed）
T = [[] for _ in range(N * K)]
for _ in range(N * K - 1):
    u, v = map(lambda x: int(x) - 1, input().split())  # 入力は1-indexedなので -1
    T[u].append(v)
    T[v].append(u)

# 非再帰DFSのためのスタック
# 各要素は (現在の頂点 v, 親 p, 処理状態 t) のタプル
st = [(0, -1, 0)]  # 0 を根として開始

# 部分木サイズを管理する配列
size = [1] * (N * K)  # 初期値 1（自身を含む）

while st:
    v, p, t = st.pop()

    if t == 0:
        # 子の処理前
        st.append((v, p, 1))  # 子の処理後に戻るフラグ
        for u in T[v]:
            if u != p:
                st.append((u, v, 0))  # 子ノードをスタックに追加
    else:
        # 子の処理後
        cnt = 0  # このノードの子でサイズ > 0 のものの数
        for u in T[v]:
            if u != p:
                size[v] += size[u]  # 子のサイズを合算
                if size[u] > 0:
                    cnt += 1  # 実際にまだ分解されていない子を数える

        # ここから条件チェック
        if size[v] > K or cnt >= 3:
            # 部分木のサイズが K より大きい or 子が3つ以上残っている場合は分解不可能
            print("No")
            exit()
        if size[v] < K and cnt >= 2:
            # サイズが K 未満なのに、子が2つ以上残っているとパスにならない
            print("No")
            exit()
        if size[v] == K:
            # サイズが K ちょうどなら、この部分木を「取り除いた」扱いにする
            size[v] = 0

# 全てのノードで条件をクリアした場合
print("Yes")
