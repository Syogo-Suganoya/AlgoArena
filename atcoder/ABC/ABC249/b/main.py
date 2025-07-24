s = input()
slist = list(s)

if not s.islower() and not s.isupper() and len(slist) == len(set(slist)):
    print("Yes")
else:
    print("No")
