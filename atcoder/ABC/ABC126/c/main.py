N, K = map(int, input().split())

ans = 0.0
for i in range(1, N + 1):
    score = i
    cnt = 0
    while score < K:
        score *= 2
        cnt += 1
    # サイコロで i が出る確率 1/N、コインで cnt 回連続で表が出る確率 (1/2)^cnt
    ans += (1 / N) * (0.5**cnt)

print(ans)
