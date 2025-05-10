S = input()


def main():
    bl = S.index("B")
    br = S.rindex("B")
    if bl % 2 == br % 2:
        return False

    rl = S.index("R")
    rr = S.rindex("R")
    k = S.index("K")
    if not (rl < k < rr):
        return False

    return True


print("Yes" if main() else "No")
