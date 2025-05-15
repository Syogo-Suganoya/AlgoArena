X = input()


def main():
    if int(X) % 1111 == 0:
        return False

    for i in range(3):
        if int(X[i + 1]) - int(X[i]) not in [1, -9]:
            return True
    return False


print("Strong" if main() else "Weak")
