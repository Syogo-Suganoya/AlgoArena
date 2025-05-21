A, B, C = map(int, input().split())

found = False
# B - 1 までの間で周期的に変化
for i in range(B):
    # S mod B = C
    if (A * i) % B == C:
        found = True
        break

print("YES" if found else "NO")
