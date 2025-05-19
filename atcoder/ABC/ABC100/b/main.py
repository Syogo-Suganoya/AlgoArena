D, N = map(int, input().split())

# 100は、ちょうど D+1 回割りきれる正の整数になるため、スキップ
if N == 100:
    N += 1

print((100**D) * N)
