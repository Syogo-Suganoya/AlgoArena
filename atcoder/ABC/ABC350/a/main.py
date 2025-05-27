S = input()


def main():
    if S == "ABC316":
        return False
    return 0 < int(S[-3:]) < 350


print("Yes" if main() else "No")
