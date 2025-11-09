S = input()

l = []
tmp = []

for i, c in enumerate(S):
    if c == ".":
        continue

    tmp.append(i + 1)

    # tmp に 2 つの要素がたまったら l に追加してリセット
    if len(tmp) == 2:
        l.append(tuple(tmp))
        tmp = []

for a, b in l:
    print(f"{a},{b}")
