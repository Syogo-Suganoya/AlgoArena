def main():
    _, X, Y, Z = map(int, input().split())

    start = min(X, Y)
    end = max(X, Y)

    return start <= Z <= end


print("Yes" if main() else "No")
