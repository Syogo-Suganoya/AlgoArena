H, W = map(int, input().split())
R, C = map(int, input().split())

cnt = 4

if R == 1:
    cnt -= 1
if R == H:
    cnt -= 1
if C == 1:
    cnt -= 1
if C == W:
    cnt -= 1

print(cnt)
