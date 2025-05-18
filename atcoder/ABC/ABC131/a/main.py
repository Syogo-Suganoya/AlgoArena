S = input()


def main():
    for i in range(3):
        if S[i] == S[i + 1]:
            return False
    return True


print("Good" if main() else "Bad")
