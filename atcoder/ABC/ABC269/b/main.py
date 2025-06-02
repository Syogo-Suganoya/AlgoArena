A = [list(input()) for _ in range(10)]

min_i, max_i = 10, -1
min_j, max_j = 10, -1

for i in range(10):
    for j in range(10):
        if A[i][j] == "#":
            min_i = min(min_i, i)
            max_i = max(max_i, i)
            min_j = min(min_j, j)
            max_j = max(max_j, j)

print(min_i + 1, max_i + 1)
print(min_j + 1, max_j + 1)
