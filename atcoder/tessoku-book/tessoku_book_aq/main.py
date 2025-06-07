N, L = map(int, input().split())
max_time = 0

for _ in range(N):
    A, B = input().split()
    A = int(A)
    if B == "E":
        time = L - A
    else:
        time = A
    max_time = max(max_time, time)

print(max_time)
