S = input()


def main():
    return len(S) == len(set(S))


print("yes" if main() else "no")
