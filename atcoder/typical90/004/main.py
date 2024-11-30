H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

yoko = list(map(sum, A))
tate = list(map(sum, zip(*A)))

for i in range(H):
    for j in range(W):
        print(yoko[i] + tate[j] - A[i][j], end=" ")
    print()
