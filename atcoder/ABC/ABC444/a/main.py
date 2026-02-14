def main():
    N = input()
    return len(set(list(N))) == 1


print("Yes" if main() else "No")
