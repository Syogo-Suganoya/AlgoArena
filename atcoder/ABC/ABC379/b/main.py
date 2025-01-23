N, K = map(int, input().split())
S = input()

res = 0
i = 0
while i < N - K + 1:
    if "X" not in S[i:i + K]:
        res += 1
        i += K
        continue
    i += 1

print(res)
