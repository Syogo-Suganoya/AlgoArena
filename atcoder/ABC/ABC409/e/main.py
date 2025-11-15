# ノード数と各ノードの値を入力
N = int(input())
x = list(map(int, input().split()))  # x[i] はノード i の値

# 木を隣接リストで表現
T = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1  # 0-indexed に変換
    v -= 1
    # 無向グラフなので両方向に追加
    T[u].append((v, w))
    T[v].append((u, w))

# 最終的なコストの合計
ans = 0

# スタックを使った非再帰 DFS
# スタックの要素は (現在のノード, 親ノード, 状態)
# 状態 t=0: 子ノードを探索する前
# 状態 t=1: 子ノードを探索した後
st = [(0, -1, 0)]  # 根ノード 0 から開始。親は -1

while st:
    v, p, t = st.pop()
    if t == 0:
        # 子ノード探索前
        st.append((v, p, 1))  # 探索後に処理するため再度プッシュ
        for u, w in T[v]:
            if u != p:  # 親ノードには戻らない
                st.append((u, v, 0))  # 子ノードを探索
    else:
        # 子ノード探索後
        for u, w in T[v]:
            if u == p:
                continue  # 親ノードは無視
            # 子ノードの値を親ノードに送るコストを加算
            ans += w * abs(x[u])
            # 子ノードの値を親ノードに集約
            x[v] += x[u]

# 最終的に根ノードに全ての値が集まり、ans が合計コスト
print(ans)
