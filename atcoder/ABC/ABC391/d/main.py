# 公式解説から引用
# https://atcoder.jp/contests/abc391/editorial/12102

N, W = map(int, input().split())  # ブロックの数 N、グリッドの幅 W

X = [0] * N  # 各ブロックの x 座標
Y = [0] * N  # 各ブロックの y 座標
blocks = [[] for _ in range(W + 1)]  # 各 x 座標ごとにブロックを格納するリスト


for i in range(N):
    X[i], Y[i] = map(int, input().split())
    blocks[X[i]].append((Y[i], i))  # X[i] の列にブロックを追加

cnt = [0] * N  # 各ブロックの "何番目に上にあるか" を記録
disappear = [-1] * (N + 1)  # 各高さのブロックが "いつ消えるか" を管理

for x in range(1, W + 1):
    blocks[x].sort(key=lambda p: p[0])  # Y座標でソート
    for j, (y, i) in enumerate(blocks[x]):
        cnt[i] = j  # ブロック i は j 番目に上にある
        disappear[j] = max(disappear[j], y)  # 高さ j の消滅時刻を更新
    disappear[len(blocks[x])] = 10**10  # 存在しない高さは無限大に設定

for i in range(N):
    disappear[i + 1] = max(disappear[i + 1], disappear[i] + 1)

Q = int(input())
for _ in range(Q):
    T, A = map(int, input().split())
    A -= 1  # 0-indexed に修正
    print("Yes" if T < disappear[cnt[A]] else "No")
