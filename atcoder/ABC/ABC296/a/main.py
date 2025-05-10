N = int(input())
S = input()


def main():
    for i in range(1, N):
        if S[i] == S[i - 1]:
            return False
    return True


print("Yes" if main() else "No")
