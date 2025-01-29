N = int(input())
S = input()


def main():
    now = (0, 0)
    s = set()
    s.add(now)
    for i in S:
        match i:
            case "L":
                next = (now[0], now[1] - 1)
            case "R":
                next = (now[0], now[1] + 1)
            case "U":
                next = (now[0] - 1, now[1])
            case "D":
                next = (now[0] + 1, now[1])
        if next in s:
            return True
        now = next
        s.add(now)

    return False


print("Yes" if main() else "No")
