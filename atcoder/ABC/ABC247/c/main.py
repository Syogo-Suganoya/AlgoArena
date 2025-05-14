def generate_sequence(n):
    """再帰的に数列を生成する関数"""
    if n == 1:
        return "1"
    prev = generate_sequence(n - 1)
    return f"{prev} {n} {prev}"


N = int(input())
result = generate_sequence(N)
print(result)
