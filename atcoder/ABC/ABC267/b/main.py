def search(column):
    for i in range(7):
        for j in range(i):
            if column[i] and column[j]:
                for k in range(j + 1, i):
                    if not column[k]:
                        return "Yes"
    return "No"


s = input()
s = "$" + s

if s[1] == "1":
    print("No")
else:
    column = [False] * 7
    column[0] = s[7] == "1"
    column[1] = s[4] == "1"
    column[2] = (s[2] == "1") or (s[8] == "1")
    column[3] = (s[1] == "1") or (s[5] == "1")
    column[4] = (s[3] == "1") or (s[9] == "1")
    column[5] = s[6] == "1"
    column[6] = s[10] == "1"
    print(search(column))
