N, K = map(int, input().split())
A = list(map(int, input().split()))

A = set(A)
A = {a for a in A if a <= K}

total = K * (K + 1) // 2
sum_a = sum(A)

print(total - sum_a)
