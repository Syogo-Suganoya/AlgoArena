N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

max_t = 0
max_1 = 0
pos_t = None
pos_1 = None
for i in range(N):
    if C[i] == T:
        if max_t < R[i]:
            max_t = R[i]
            pos_t = i + 1
    if C[i] == C[0]:
        if max_1 < R[i]:
            max_1 = R[i]
            pos_1 = i + 1
print(pos_t or pos_1)
