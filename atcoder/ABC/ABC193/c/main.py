N = int(input())
s = set()

# i のべき乗で N 以下になる限界まで
for i in range(2, int(N**0.5) + 1):
    for j in range(2, 100):  # j=2 から十分大きい上限まで
        v = i**j
        if v > N:
            break
        s.add(v)

print(N - len(s))
