a, b = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

like = max(A)


def main():
    for i in B:
        if A[i - 1] == like:
            print("Yes")
            return
    print("No")


main()
