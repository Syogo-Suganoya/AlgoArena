N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 累積和：1と0の出現回数を記録
count_1 = [0] * (N + 1)
count_0 = [0] * (N + 1)

for i in range(N):
    count_1[i + 1] = count_1[i] + (1 if A[i] == 1 else 0)
    count_0[i + 1] = count_0[i] + (1 if A[i] == 0 else 0)

# クエリ処理
for _ in range(Q):
    L, R = map(int, input().split())
    one = count_1[R] - count_1[L - 1]
    zero = count_0[R] - count_0[L - 1]

    if one > zero:
        print("win")
    elif one == zero:
        print("draw")
    else:
        print("lose")
