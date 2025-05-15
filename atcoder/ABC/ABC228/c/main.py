N, K = map(int, input().split())
l = []
for i in range(N):
    P = list(map(int, input().split()))
    l.append(sum(P))

border = sorted(l, reverse=True)[K - 1]

for i in l:
    if i + 300 >= border:
        print("Yes")
    else:
        print("No")
