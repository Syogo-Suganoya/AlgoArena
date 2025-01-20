k = int(input())

ans = 0
for a in range(1, k + 1):
    if a**3 > k:
        break
    if k % a > 0:
        continue
    for b in range(a, k + 1):
        if a * b * b > k:
            break
        if (k // a) % b > 0:
            continue
        c = k // a // b
        if c >= b:
            ans += 1
print(ans)
