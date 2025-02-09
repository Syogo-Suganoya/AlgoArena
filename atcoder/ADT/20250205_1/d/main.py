S = input()

count_u = sum(1 for c in S if c.isupper())
count_l = sum(1 for c in S if c.islower())
if count_u > count_l:
    print(S.upper())
else:
    print(S.lower())
