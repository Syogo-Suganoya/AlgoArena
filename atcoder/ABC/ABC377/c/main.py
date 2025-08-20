N, M = map(int, input().split())

cell = set()
vec = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

for i in range(M):
    a, b = map(int, input().split())
    cell.add((a, b))
    for vec_i in vec:
        vec_a = a + vec_i[0]
        vec_b = b + vec_i[1]
        if 1 <= vec_a and vec_a < N + 1:
            if 1 <= vec_b and vec_b < N + 1:
                cell.add((vec_a, vec_b))

print(N**2 - len(cell))
