from math import factorial

H, W = map(int, input().split())

result = factorial(H + W) // (factorial(H) * factorial(W))

print(result % 1000000007)
