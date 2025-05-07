import bisect

M = int(input())
D = list(map(int, input().split()))

t = sum(D)
half = int((t + 1) / 2)

cumsum = [0] * (M + 1)
for i, num in enumerate(D):
    cumsum[i + 1] = cumsum[i] + num

pos1 = bisect.bisect_left(cumsum, half)

print(pos1, half - cumsum[pos1 - 1])
