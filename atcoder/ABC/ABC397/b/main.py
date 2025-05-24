S = input()
ans = 0
targets = "io"
target = targets[0]
for c in S:
    if c == target:
        target = targets[(targets.index(target) + 1) % 2]
    else:
        ans += 1
if target == "o":
    ans += 1
print(ans)
