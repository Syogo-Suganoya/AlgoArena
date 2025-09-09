N = int(input())
s = set()
for i in range(N):
    A, B = map(str, input().split())
    if (A, B) in s:
        print("Yes")
        break
    s.add((A, B))
else:
    print("No")
