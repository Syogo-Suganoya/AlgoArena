N = int(input())

i = 0
res = -1

while True:
    a = i**3
    if a > N:
        break
    if str(a) == str(a)[::-1]:
        res = a
    i += 1

print(res)
