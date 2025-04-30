def main():
    A, B, C = map(int, input().split())
    if B > C:
        C += 24
    if A < B:
        A += 24
    return not (B <= A <= C)


print("Yes" if main() else "No")
