N = int(input())
A = [None] + list(map(int, input().split()))

# A に登場する値を記録
appeared = set(A)

# N 以下で A に登場しない値を探す
start = -1
for i in range(1, N + 1):
    if i not in appeared:
        start = i
        break

# 辿る部分
res = []
val = start
while val != -1:
    res.append(val)
    val = A[val]

res.reverse()
print(*res)
