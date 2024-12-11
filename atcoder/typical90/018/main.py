import math


def query(I, T, L, X, Y):
    PI = math.pi
    cx = 0
    cy = -(L / 2.0) * math.sin(I / T * 2.0 * PI)
    cz = (L / 2.0) - (L / 2.0) * math.cos(I / T * 2.0 * PI)
    d1 = math.sqrt((cx - X) ** 2 + (cy - Y) ** 2)
    d2 = cz
    kaku = math.atan2(d2, d1)
    return kaku * 180.0 / PI


def main():
    T = float(input())
    L, X, Y = map(float, input().split())
    Q = int(input())
    results = []
    for _ in range(Q):
        E = float(input())
        results.append(query(E, T, L, X, Y))

    for result in results:
        print(f"{result:.12f}")


if __name__ == "__main__":
    main()
