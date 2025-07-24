x1, y1, x2, y2 = list(map(int, input().split()))


def f(xa, ya, xb, yb):
    return (xa - xb) ** 2 + (ya - yb) ** 2


def main():
    for i in range(-2, 3):
        for j in range(-2, 3):
            xi = x1 + i
            yj = y1 + j

            if f(xi, yj, x1, y1) == 5 and f(xi, yj, x2, y2) == 5:
                return True
    return False


print("Yes" if main() else "No")
