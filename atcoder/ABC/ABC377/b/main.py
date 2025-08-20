S = []

for i in range(8):
    S.append(list(input()))
rows_to_mark = set()
cols_to_mark = set()
for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            rows_to_mark.add(i)
            cols_to_mark.add(j)
for i in range(8):
    for j in range(8):
        if i in rows_to_mark or j in cols_to_mark:
            S[i][j] = "-"
res = 0
for row in S:
    res += row.count(".") + row.count("#")
print(res)
