def main():
    N = int(input())
    b = None
    for i in range(N - 1):
        S = input()

        if b == "sweet" and S == "sweet":
            return False
        b = S

    return True


print("Yes" if main() else "No")
