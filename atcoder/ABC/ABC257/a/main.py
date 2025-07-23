n, x = map(int, input().split())
s = []
for i in range(ord("A"), ord("Z") + 1):
    for j in range(n):
        s.append(chr(i))
print(s[x - 1])
