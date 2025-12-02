S = list(input())


def main():
    return len(set(S)) == 1


print("Won" if main() else "Lost")
