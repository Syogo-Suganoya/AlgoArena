A, B = input().split()


def main():
    for i in range(1, min(len(A), len(B)) + 1):
        if int(A[-i]) + int(B[-i]) >= 10:
            return False
    return True


print("Easy" if main() else "Hard")
