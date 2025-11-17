N, K = map(int, input().split())
A = list(map(int, input().split()))
dis = 1
for a in A:
    dis *= a
    if len(str(dis)) > K:
        dis = 1

print(dis)
