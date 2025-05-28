S = input()


def main():
    # 先頭末尾が<>でないならFalse
    if S[0] != "<" or S[-1] != ">":
        return False

    # 中間が=のみでないならFalse
    middle = S[1:-1]
    if not all(c == "=" for c in middle):
        return False

    return True


print("Yes" if main() else "No")
