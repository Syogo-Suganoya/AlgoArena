A, B, C, D = map(int, input().split())


def main():
    if C < A:
        return True
    return B <= D


print("No" if main() else "Yes")
