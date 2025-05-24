a, b, c = map(int, input().split())
if c == 1:
    ans = "No"
else:
    b = min(b, 60)  # 2^60で十分aを超える
    if a < pow(c, b):
        ans = "Yes"
    else:
        ans = "No"

print(ans)
