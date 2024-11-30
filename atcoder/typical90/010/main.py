N = int(input())

cumsum1 = [0] * (N + 1)
cumsum2 = [0] * (N + 1)

C, P = [], []
for i in range(1, N + 1):
    C, P = map(int, input().split())
    cumsum1[i] = cumsum1[i - 1]
    cumsum2[i] = cumsum2[i - 1]
    if C == 1:
        cumsum1[i] += P
    else:
        cumsum2[i] += P

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(cumsum1[R] - cumsum1[L - 1], cumsum2[R] - cumsum2[L - 1])
