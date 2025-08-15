S = input()

# 'a' から 'z' までループ
for c in "abcdefghijklmnopqrstuvwxyz":
    if c not in S:
        print(c)
        break
