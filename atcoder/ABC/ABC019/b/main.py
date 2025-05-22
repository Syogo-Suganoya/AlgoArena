from itertools import groupby

S = input()
print("".join(f"{char}{len(list(group))}" for char, group in groupby(S)))
