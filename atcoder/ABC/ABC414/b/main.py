N = int(input())
ans = ""
for i in range(N):
    c, l = map(str, input().split())
    l = int(l)
    if len(ans) + l > 100:
        print("Too Long")
        break
    ans += c * int(l)
else:
    if len(ans) > 100:
        ans = "Too Long"
    print(ans)
