W, a, b = map(int, input().split())
l = min(a, b)
r = max(a, b)
print(max(0, r - W - l))
