a, b = map(int, input().split())


def main():
    return (a * b) % 2 == 0


print("Even" if main() else "Odd")
