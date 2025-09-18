import heapq

N, M = map(int, input().split())
jobs = [tuple(map(int, input().split())) for _ in range(N)]  # (A, B)

# 日ごとに受けられる仕事をまとめる（A日以内に始めないといけない）
# job_by_day[d] = d日目までに始めれば間に合う仕事の報酬リスト
job_by_day = [[] for _ in range(M + 1)]
for a, b in jobs:
    if a <= M:  # M日以内に終えられる仕事だけが対象
        job_by_day[a].append(b)

# 最大ヒープ (Python の heapq は最小ヒープなので -値で管理)
heap = []
ans = 0

# 1日目からM日目まで進める
for day in range(1, M + 1):
    # この日に開始可能になった仕事をヒープに追加
    for b in job_by_day[day]:
        heapq.heappush(heap, -b)

    # できる仕事があれば、最も報酬の大きいものを選ぶ
    if heap:
        ans += -heapq.heappop(heap)

print(ans)
