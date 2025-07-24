T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    ans = "No"
    if 2 * a <= s:
        differ = s - 2 * a
        if (differ & a) == 0:
            ans = "Yes"
    print(ans)
