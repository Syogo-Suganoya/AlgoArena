from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

rem_counts = [defaultdict(int) for _ in range(12)]
for a in A:
    for k in range(1, 11):  # 桁数 1 から 10 まで
        r = (a * pow(10, k, M)) % M
        rem_counts[k][r] += 1

ans = 0
for a in A:
    len_a = len(str(a))
    target_rem = (M - (a % M)) % M
    ans += rem_counts[len_a][target_rem]

print(ans)
