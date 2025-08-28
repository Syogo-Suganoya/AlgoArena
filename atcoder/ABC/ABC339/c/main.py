N = int(input())
A = list(map(int, input().split()))

cum = [0]
for a in A:
    cum.append(cum[-1] + a)

init = min(0, min(cum))
print(-init + cum[-1])
