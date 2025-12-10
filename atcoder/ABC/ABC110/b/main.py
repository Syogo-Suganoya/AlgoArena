N, M, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxA = max(A)
minB = min(B)

# Z が入れる区間
left = max(maxA, X)
right = min(minB, Y)

# 区間 (left, right] に整数が存在するか？
if left < right:
    print("No War")
else:
    print("War")
