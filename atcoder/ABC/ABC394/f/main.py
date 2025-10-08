from collections import deque

# 入力：頂点数 n
n = int(input())
# 隣接リストで木を表現
v = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1  # 0-indexed に変換
    v[a].append(b)
    v[b].append(a)

# DFS用のスタック（deque）
# q: 現在のノード, w: 親ノード, e: 子リストの処理インデックス
f = deque([[0, -1, 0]])

# 各ノードの部分木の最大深さを格納するリスト
c = [1] * n

# 答え（条件を満たす最大値）初期化
ans = -1

while f:
    q, w, e = f.pop()  # スタックから取り出し
    if len(v[q]) > e:
        # qの子リストにまだ処理していない子がある場合
        f.append([q, w, e + 1])  # 次の子の処理用に再びスタックに追加
        if v[q][e] == w:
            # 子が親だった場合はスキップ
            continue
        # 子ノードを処理するためスタックに追加
        f.append([v[q][e], q, 0])
    else:
        # qのすべての子の処理が終わった段階
        if len(v[q]) >= 4:
            # 子が4人以上いる場合、最大4本の部分木の深さを使用
            s = []
            for i in v[q]:
                if i == w:
                    # 親ノードは深さとして使わない
                    s.append(1)
                    continue
                s.append(c[i])
            # 深い順にソート
            s.sort(reverse=True)
            # 上位4本の部分木の深さの合計＋1を計算し最大値を更新
            ans = max(ans, sum(s[:4]) + 1)
            # 現在ノード q の部分木の深さは上位3本の合計＋1
            c[q] = sum(s[:3]) + 1

# 結果出力
print(ans)
