N, K = map(int, input().split())
A = list(map(int, input().split()))

unique_A = set(A)
mex = 0
while mex in unique_A and mex < K:
    mex += 1

print(mex)
