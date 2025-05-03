def main():
    S = list(input())

    index_r = S.index("R")
    index_m = S.index("M")

    return index_r < index_m


print("Yes" if main() else "No")
