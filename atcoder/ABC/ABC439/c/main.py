N = int(input())

# c[n] = 「n を x^2 + y^2 (x < y) で表せる回数」
c = [0] * (N + 1)

# x < y になるように回す
x = 1
while x * x <= N:
    y = x + 1
    while x * x + y * y <= N:
        c[x * x + y * y] += 1
        y += 1
    x += 1

# ちょうど1回だけ表せる数を集める
ans = []
for n in range(1, N + 1):
    if c[n] == 1:
        ans.append(n)

# 出力
print(len(ans))
print(*ans)
