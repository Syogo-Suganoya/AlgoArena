from math import factorial

H, W = map(int, input().split())

# 経路数 = (H+W-2)! / ((H-1)! * (W-1)!)
result = factorial(H + W - 2) // (factorial(H - 1) * factorial(W - 1))

print(result % 1000000007)
