N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 差分配列Bの初期化
B = [0] * (N + 1)
for i in range(1, N):
    B[i] = A[i] - A[i - 1]

# 初期の総コスト計算
Answer = sum(abs(B[i]) for i in range(1, N))

# クエリ処理
for L, R, V in queries:
    # 現在のL-1とRの差分コストを計算
    before = 0
    if L >= 2:
        before += abs(B[L - 1])
    if R <= N - 1:
        before += abs(B[R])

    # 差分配列を更新
    if L >= 2:
        B[L - 1] += V
    if R <= N - 1:
        B[R] -= V

    # 更新後のL-1とRの差分コストを計算
    after = 0
    if L >= 2:
        after += abs(B[L - 1])
    if R <= N - 1:
        after += abs(B[R])

    # 総コストを更新して出力
    Answer += after - before
    print(Answer)
