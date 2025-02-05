A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


def main():
    def cross_product(u, v):
        return u[0] * v[1] - u[1] * v[0]

    def vector(p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])

    AB = vector(A, B)
    BC = vector(B, C)
    CD = vector(C, D)
    DA = vector(D, A)

    cross_products = [
        cross_product(AB, BC),
        cross_product(BC, CD),
        cross_product(CD, DA),
        cross_product(DA, AB),
    ]

    return all(cp > 0 for cp in cross_products)


print("Yes" if main() else "No")
