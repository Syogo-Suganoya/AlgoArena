A = list(map(int, input().split()))
S = input()

l = ["Red", "Green", "Blue"]
A[l.index(S)] = 101
print(min(A))
