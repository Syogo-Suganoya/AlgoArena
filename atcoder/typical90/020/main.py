a, b, c = map(int, input().split())

l = a
r = c**b

print("Yes" if l < r else "No")
