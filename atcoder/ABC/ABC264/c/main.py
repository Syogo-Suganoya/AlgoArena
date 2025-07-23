from itertools import combinations

H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

# Aの中からH2個の行、W2個の列を選んで試す
for rows in combinations(range(H1), H2):
    for cols in combinations(range(W1), W2):
        # rowsとcolsで選んだ部分行列を作成
        submatrix = [[A[r][c] for c in cols] for r in rows]
        if submatrix == B:
            print("Yes")
            exit()

print("No")
