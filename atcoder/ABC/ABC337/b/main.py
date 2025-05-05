def f(pos1, pos2):
    if pos1 and pos2:
        return pos1 > pos2


S = input()
pos_a = None
pos_b = None
pos_c = None
for i, c in enumerate(S, 1):
    match c:
        case "A":
            pos_a = i
        case "B":
            pos_b = i
        case "C":
            pos_c = i

    if f(pos_a, pos_b):
        print("No")
        break

    if f(pos_b, pos_c):
        print("No")
        break

    if f(pos_a, pos_c):
        print("No")
        break

else:
    print("Yes")
