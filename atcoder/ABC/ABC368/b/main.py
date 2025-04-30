N = int(input())
A = list(map(int, input().split()))

res = 0

while sum(1 for x in A if x > 0) > 1:
    A = sorted(A, reverse=True)
    A[0] -= 1
    A[1] -= 1
    res += 1

print(res)

"""
N = int(input())
A = list(map(int, input().split()))
res =0
Aの値のうち、自然数が1こ以下になるまで
    Aをソート
    A[0:1]を-=1
    res +=1
print(res)
"""
