N, W = map(int, input().split())
cheeses = []

for _ in range(N):
    A, B = map(int, input().split())
    cheeses.append((A, B))

# 1gあたりの美味しさが高い順にソート
cheeses.sort(reverse=True)

total_deliciousness = 0
remaining_weight = W

for A, B in cheeses:
    if remaining_weight == 0:
        break
    # 使用する量は、残りの許容量とBの小さい方
    use = min(B, remaining_weight)
    total_deliciousness += A * use
    remaining_weight -= use

print(total_deliciousness)
