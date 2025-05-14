N = int(input())
H = list(map(int, input().split()))

res = -0
for i in H:
    if i <= res:
        break
    res = i
print(res)
