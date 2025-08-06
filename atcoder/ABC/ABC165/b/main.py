X = int(input())

x = 100
ans = 0

while x < X:
    x += x // 100  # 年利1%の複利（整数部分のみ）
    ans += 1

print(ans)
