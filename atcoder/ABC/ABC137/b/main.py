K, X = map(int, input().split())
l = []
for i in range(X - K + 1, X + K):
    l.append(i)

print(*l)
