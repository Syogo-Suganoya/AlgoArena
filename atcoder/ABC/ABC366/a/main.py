def main():
    N, T, A = map(int, input().split())

    stock = N - T - A
    lesser = min(T, A)
    greater = max(T, A)

    return greater > lesser + stock


print("Yes" if main() else "No")
