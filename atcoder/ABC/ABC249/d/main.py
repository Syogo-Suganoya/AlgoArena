def Divisors(N):
    N = abs(N)
    L, U = [], []
    k = 1
    while k * k <= N:
        if N % k == 0:
            L.append(k)
            if k * k != N:
                U.append(N // k)
        k += 1
    return L + U[::-1]


N = int(input())
A = list(map(int, input().split()))

M = max(A)
chi = [0] * (M + 1)
for a in A:
    chi[a] += 1

X = 0
for a in range(1, M + 1):
    for b in Divisors(a):
        c = a // b
        X += chi[a] * chi[b] * chi[c]

print(X)
