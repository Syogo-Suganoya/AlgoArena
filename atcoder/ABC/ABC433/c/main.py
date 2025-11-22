S = input()

RLE = []
cnt = 1
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        cnt += 1
    else:
        RLE.append((S[i - 1], cnt))
        cnt = 1
RLE.append((S[-1], cnt))

ans = 0
for i in range(1, len(RLE)):
    if int(RLE[i][0]) - int(RLE[i - 1][0]) == 1:
        ans += min(RLE[i - 1][1], RLE[i][1])

print(ans)
