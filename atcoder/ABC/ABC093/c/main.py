A, B, C = map(int, input().split())
M = max(A, B, C)
S = A + B + C

for i in range(0, 1000):
    X = M + i
    delta = 3 * X - S
    if delta % 2 == 0:
        print(delta // 2)
        break
