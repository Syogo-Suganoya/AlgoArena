N = int(input())
A = list(map(int, input().split()))

pairs = [(val, idx) for idx, val in enumerate(A, start=1)]
pairs.sort()
ans = [str(pairs[i][1]) for i in range(3)]
print(" ".join(ans))
