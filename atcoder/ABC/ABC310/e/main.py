N = int(input())
A = input()

zero, one = 0, 0
ans = 0

for a in A:
    if a == "0":
        zero, one = 1, zero + one
    else:
        zero, one = one, zero + 1
    ans += one

print(ans)
