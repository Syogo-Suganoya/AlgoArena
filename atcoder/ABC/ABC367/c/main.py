"""
制約が小さいため、全探索（再帰 or DFS）で解くことができる。
各位置 i において 1〜Ri の値を順に選びながら列を構築し、
最後に和が K の倍数ならば出力する。
"""

N, K = map(int, input().split())
R = list(map(int, input().split()))


def dfs(i, seq, total):
    """
    i: 現在見ているインデックス（0始まり）
    seq: これまでに選んだ数列（リスト）
    total: 現在の合計値
    """
    if i == N:
        if total % K == 0:
            print(" ".join(map(str, seq)))
        return
    for val in range(1, R[i] + 1):
        dfs(i + 1, seq + [val], total + val)


dfs(0, [], 0)
