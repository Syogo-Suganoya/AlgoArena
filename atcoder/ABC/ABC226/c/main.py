import sys

sys.setrecursionlimit(1 << 25)  # 再帰が深くなる可能性があるので、上限を引き上げる


N = int(input())  # 技の数
T = [0] * N  # 各技の習得時間（T[i] は技 i+1 に対応）
G = [[] for _ in range(N)]  # 技の依存関係を格納する隣接リスト（有向グラフ）


# 技 v を習得するために必要なすべての技を DFS で辿る
def dfs(v):
    if seen[v]:
        return  # すでに習得済みなら何もしない
    seen[v] = True  # 技 v を習得済としてマーク
    for u in G[v]:  # 技 v に依存する技 u を順に辿る
        dfs(u)


for i in range(N):
    tmp = list(map(int, input().split()))  # 入力：T[i], K[i], A[i][0], ..., A[i][K-1]
    T[i] = tmp[0]  # 技 i+1 を習得するのにかかる時間
    K = tmp[1]  # 技 i+1 に必要な事前技の個数
    if K > 0:
        G[i] = [a - 1 for a in tmp[2:]]  # 0-indexed に変換して格納

seen = [False] * N  # 技 i をすでに習得済（または調査済）かを管理するフラグ
dfs(N - 1)  # 最後の技（技 N）を習得するために必要な技をすべて調べる
ans = 0
for i in range(N):
    if seen[i]:  # 習得が必要な技であれば
        ans += T[i]  # 習得時間を加算
print(ans)  # 技 N を習得するために必要な最小合計時間
