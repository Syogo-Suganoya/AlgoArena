import sys

sys.setrecursionlimit(10**7)

N = int(input())
# A[i][j] = 人iと人jをペアにしたときの楽しさ（XORで使う値）
A = [[0] * (2 * N) for _ in range(2 * N)]

# 入力は上三角だけ与えられるので、左右対称に埋める
for i in range(2 * N - 1):
    line = list(map(int, input().split()))
    for j, v in enumerate(line, start=i + 1):
        A[i][j] = v
        A[j][i] = v  # 対称に代入

used = [False] * (2 * N)  # すでにペアにした人を管理
ans = 0  # 最大値


def dfs(current_xor):
    """今まで作ったペアのXOR合計がcurrent_xorの状態から再帰的に探索する"""
    global ans

    # まだペアにしてない人を探す
    first = -1
    for i in range(2 * N):
        if not used[i]:
            first = i
            break

    # 全員ペアにしたら最大値を更新
    if first == -1:
        ans = max(ans, current_xor)
        return

    # first を使うと決めて、その相手を j としてループ
    used[first] = True
    for j in range(first + 1, 2 * N):
        if not used[j]:
            used[j] = True
            # first と j をペアにした → XORを追加して次へ
            dfs(current_xor ^ A[first][j])
            used[j] = False
    used[first] = False


dfs(0)
print(ans)
