S = input()

N = int(S[0])
M = int(S[-1])

if M == 8:
    M = 1
    N += 1
else:
    M += 1
print(f"{N}-{M}")
