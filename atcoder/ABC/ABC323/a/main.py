def main():
    S = input()
    even_chars = S[1::2]
    i = int(even_chars)
    return i == 0


print("Yes" if main() else "No")
