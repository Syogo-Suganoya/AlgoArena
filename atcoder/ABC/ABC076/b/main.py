N = int(input())
K = int(input())

now = 1

for i in range(N):
    if now < K:
        now *= 2
    else:
        now += K
print(now)
