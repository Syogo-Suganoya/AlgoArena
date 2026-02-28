S = input()
T = input()

if S.replace("A", "") != T.replace("A", ""):
    print(-1)
    exit()

i = 0
j = 0
ops = 0

while i < len(S) or j < len(T):
    if i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            if S[i] == "A":
                i += 1
                ops += 1
            else:
                j += 1
                ops += 1

    elif i < len(S):
        ops += 1
        i += 1
    else:
        ops += 1
        j += 1

print(ops)
