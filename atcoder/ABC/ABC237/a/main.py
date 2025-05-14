N = int(input())


def main():
    return -(2**31) <= N < 2**31


print("Yes" if main() else "No")
