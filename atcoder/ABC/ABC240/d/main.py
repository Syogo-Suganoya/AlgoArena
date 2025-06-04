N = int(input())
A = list(map(int, input().split()))
l = []
ans = 0

for a in A:
    ans += 1
    if l and l[-1][0] == a:
        l[-1][1] += 1
        if l[-1][1] == a:
            ans -= a
            l.pop()
    else:
        l.append([a, 1])
    print(ans)
