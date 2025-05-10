S = input()


def main():
    for i, c in enumerate(S):
        if c.isupper():
            print(i + 1)
            return


main()
