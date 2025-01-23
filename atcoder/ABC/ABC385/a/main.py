A, B, C = map(int, input().split())


def main():
    if A == B == C:
        return True
    if A + B == C:
        return True
    if B + C == A:
        return True
    if A + C == B:
        return True
    return False


print("Yes" if main() else "No")
