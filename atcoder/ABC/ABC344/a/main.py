S = input()

l = S.index("|")
r = S.rindex("|")

print(S[:l] + S[r + 1 :])
