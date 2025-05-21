A, B, C = input().split()


def main():
    return A[-1] == B[0] and B[-1] == C[0]


print("YES" if main() else "NO")
