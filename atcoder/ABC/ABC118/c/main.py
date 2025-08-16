from math import gcd

N = int(input())
A = list(map(int, input().split()))

result = A[0]  # 最初の要素を基準に
for i in range(1, N):
    result = gcd(result, A[i])  # 順番にGCDを更新

print(result)
