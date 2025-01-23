from collections import Counter

S = input()


def main():
    if len(S) % 2:
        return False

    if any(count != 2 for count in Counter(S).values()):
        return False

    for i in range(0, len(S) - 1, 2):
        if S[i] != S[i + 1]:
            return False

    return True


print("Yes" if main() else "No")
