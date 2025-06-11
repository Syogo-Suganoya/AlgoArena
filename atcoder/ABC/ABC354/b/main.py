N = int(input())

total_C = 0
l = []
for i in range(N):
    S, C = input().split()
    total_C += int(C)
    l.append(S)

# Sを昇順にソート
l.sort()

# インデックスを total_C % N として、その位置の S を出力
print(l[total_C % N])
