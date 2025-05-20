S = input()
for c in map(chr, range(ord("a"), ord("z") + 1)):
    if c not in S:
        print(c)
        break
else:
    print("None")
