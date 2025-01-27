A = input()


def main():
    if A == "2 1 3 4 5" or A == "1 3 2 4 5" or A == "1 2 4 3 5" or A == "1 2 3 5 4":
        return True
    return False


print("Yes" if main() else "No")
