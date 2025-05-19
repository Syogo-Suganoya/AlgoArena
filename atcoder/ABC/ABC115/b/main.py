N = int(input())
A = [int(input()) for _ in range(N)]

# 最大値を取り出して、リストから削除
p = max(A)
A.remove(p)

print(sum(A) + (p // 2))
