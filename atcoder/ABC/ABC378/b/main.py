N = int(input())
QR = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
for i in range(M):
    T, D = map(int, input().split())
    Q, R = QR[T - 1]

    quotient, mod = divmod(D, Q)

    if mod > R:
        quotient += 1
    print(quotient * Q + R)
