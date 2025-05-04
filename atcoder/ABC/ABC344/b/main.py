t = "-1"
lst = []

while t != "0":
    t = input()
    lst.append(t)

lst.reverse()

print("\n".join(lst))
