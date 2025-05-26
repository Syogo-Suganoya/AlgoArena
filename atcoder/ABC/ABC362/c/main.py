N = int(input())
al = []
bl = []

for i in range(N):
    A, B = map(int, input().split())
    al.append(A)
    bl.append(B)

ta = sum(al)

# 順番に0に近づける
for i in range(N):
    if ta >= 0:
        break
    add = min(bl[i] - al[i], abs(ta))
    if ta < 0:
        al[i] += add
        ta += add

if ta != 0:
    print("No")
else:
    print("Yes")
    print(*al)
