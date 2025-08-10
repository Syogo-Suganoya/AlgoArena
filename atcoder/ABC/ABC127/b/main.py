r, D, x = map(int, input().split())

for _ in range(10):
    x = r * x - D  # 成長モデルに従って更新
    print(x)
