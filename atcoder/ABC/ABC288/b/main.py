N, K = map(int, input().split())
l = []
for i in range(K):
    S = input()
    l.append(S)

l.sort()
print("\n".join(l))
