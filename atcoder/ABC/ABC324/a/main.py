N = int(input())
A = list(map(int, input().split()))


def main():
    return len(set(A)) == 1


print("Yes" if main() else "No")
