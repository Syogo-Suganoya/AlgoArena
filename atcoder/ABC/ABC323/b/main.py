N = int(input())
d = {}

for i in range(N):
    S = input()
    c = S.count("o")
    d[i + 1] = c

sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)

for k, _ in sorted_items:
    print(k, end=" ")
