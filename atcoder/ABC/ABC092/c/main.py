N = int(input())
A = list(map(int, input().split()))

# A₀ = 0, A_{N+1} = 0 にしておく（スタート地点とゴール地点）
A = [0] + A + [0]

# スポット全部を巡るときの合計距離 S をまず計算
S = 0
for i in range(1, N + 2):  # 0 → 1 → … → N → N+1 (=0)
    S += abs(A[i] - A[i - 1])

# i 番目（本当は A[i+1] に対応）を抜いたときの距離を順に計算
for i in range(1, N + 1):  # i は 1～N
    dist_without_i = (
        S - abs(A[i] - A[i - 1]) - abs(A[i + 1] - A[i]) + abs(A[i + 1] - A[i - 1])
    )
    print(dist_without_i)
