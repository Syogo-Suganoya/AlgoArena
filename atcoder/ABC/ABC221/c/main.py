N = sorted(input(), reverse=True)
ans = 0
for i in range(1 << len(N)):
    l = r = 0
    for j in range(len(N)):
        if i & (1 << j):
            l = l * 10 + int(N[j])
        else:
            r = r * 10 + int(N[j])
    ans = max(ans, l * r)
print(ans)
