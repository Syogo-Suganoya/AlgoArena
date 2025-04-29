N = int(input())

lst = []

for i in range(N):
    A = list(map(int, input().split()))
    lst.append(A)


x = 0
for i in range(N):
    y = i
    if x < y:
        x, y = y, x
    # print(x, y)
    x = lst[x][y] - 1

print(x + 1)
