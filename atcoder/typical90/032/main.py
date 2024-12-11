import itertools


def vaild():
    # 仲が悪いペアを確認
    for i in range(N - 1):
        if kenaku[perm[i]][perm[i + 1]]:
            return True
    return False


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
kenaku = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    X, Y = map(int, input().split())
    kenaku[X][Y] = True
    kenaku[Y][X] = True

# 全探索の準備
Answer = float("inf")
for perm in itertools.permutations(range(1, N + 1)):
    cost = 0
    if vaild():
        continue
    # 順列のコスト計算
    for i in range(N):
        cost += A[perm[i] - 1][i]
    Answer = min(Answer, cost)
# 結果の出力
print(-1 if Answer == float("inf") else Answer)
