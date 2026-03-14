N, M = map(int, input().split())
C = list(map(int, input().split()))

used = [0] * M

for _ in range(N):
    A, B = map(int, input().split())
    A -= 1
    used[A] = min(C[A], used[A] + B)

print(sum(used))
