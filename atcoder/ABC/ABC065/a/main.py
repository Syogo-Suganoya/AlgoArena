X, A, B = map(int, input().split())


def main():
    if B - A <= 0:
        print("delicious")
    elif B - A <= X:
        print("safe")
    else:
        print("dangerous")


main()
