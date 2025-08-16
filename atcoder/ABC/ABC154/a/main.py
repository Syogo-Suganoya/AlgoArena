S, T = input().split()
N, M = map(int, input().split())
U = input()

if U == S:
    N -= 1
else:
    M -= 1
print(N, M)
