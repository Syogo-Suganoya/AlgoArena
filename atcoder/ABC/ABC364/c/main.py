N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sa = sorted(A, reverse=True)
sb = sorted(B, reverse=True)

sum_a = 0
cnt_a = 0

for i in sa:
    sum_a += i
    cnt_a += 1
    if sum_a > X:
        break

sum_b = 0
cnt_b = 0

for i in sb:
    sum_b += i
    cnt_b += 1
    if sum_b > Y:
        break

print(min(cnt_a, cnt_b))
