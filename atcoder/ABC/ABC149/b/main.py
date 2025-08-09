A, B, K = map(int, input().split())

if K <= A:
    takahashi = A - K
    aoki = B
elif K <= A + B:
    takahashi = 0
    aoki = B - (K - A)
else:
    takahashi = 0
    aoki = 0

print(takahashi, aoki)
