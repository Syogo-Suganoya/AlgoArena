S1 = input()
S2 = input()


def main():
    if (S1 == "#." and S2 == ".#") or (S1 == ".#" and S2 == "#."):
        return False
    return True


print("Yes" if main() else "No")
