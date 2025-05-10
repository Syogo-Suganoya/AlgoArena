N = int(input())
S = input()


def main():
    now = (0, 0)
    s = set()
    s.add(now)

    for c in S:
        match c:
            case "R":
                now = (now[0] + 1, now[1])
            case "L":
                now = (now[0] - 1, now[1])
            case "U":
                now = (now[0], now[1] + 1)
            case "D":
                now = (now[0], now[1] - 1)

        if now in s:
            return True
        s.add(now)
    return False


print("Yes" if main() else "No")
