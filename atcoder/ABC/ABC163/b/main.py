N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)  # 宿題にかかる総日数
if total > N:
    print(-1)
else:
    print(N - total)
