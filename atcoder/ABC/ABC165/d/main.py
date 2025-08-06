A, B, N = map(int, input().split())

# N が B-1 以下ならそのまま
x = min(N, B - 1)

# f(x) の値を計算（floor 部分の差分）
answer = (A * x) // B
print(answer)
