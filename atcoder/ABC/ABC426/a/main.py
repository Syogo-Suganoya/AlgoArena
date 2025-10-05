N, M = map(str, input().split())
l = ["Ocelot", "Serval", "Lynx"]


def main():
    return l.index(N) >= l.index(M)


print("Yes" if main() else "No")
