N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

ans = sum(a * b for a, b in zip(A, B))
print(ans)
