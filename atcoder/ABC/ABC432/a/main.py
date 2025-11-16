A = list(map(int, input().split()))

A.sort(reverse=True)

print("".join(str(x) for x in A))
