N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)  # 降順で高いところから順に考える

total = 0
for i in range(0, N, D):
    # iからi+Dの範囲
    trip = F[i : i + D]
    # 部分合計がP以上ならPを採用、そうでなければそのまま
    if sum(trip) > P:
        total += P
    else:
        total += sum(trip)

print(total)
