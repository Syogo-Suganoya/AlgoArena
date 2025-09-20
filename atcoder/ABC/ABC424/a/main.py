a, b, c = map(int, input().split())


def is_triangle(a, b, c):
    # 三角不等式を満たすか確認
    return a + b > c and b + c > a and c + a > b


def main():
    return is_triangle(a, b, c) and len(set([a, b, c])) <= 2


print("Yes" if main() else "No")
