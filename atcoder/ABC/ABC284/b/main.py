N = int(input())
for _ in range(N):
    n = int(input())
    A = list(map(int, input().split()))
    odd_count = sum(1 for a in A if a % 2 == 1)
    print(odd_count)
