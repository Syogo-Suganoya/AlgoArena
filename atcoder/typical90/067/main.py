def n_to_k_base_conversion(value: str, n: int, k: int) -> str:
    decimal_value = int(value, n)
    if decimal_value == 0:
        return "0"

    result = []
    while decimal_value > 0:
        remainder = decimal_value % k
        if remainder >= 10:
            result.append(chr(ord('A') + remainder - 10))
        else:
            result.append(str(remainder))
        decimal_value //= k
    return ''.join(result[::-1])


N, K = map(int, input().split())
n = str(N)

for _ in range(K):
    n = n_to_k_base_conversion(n, 8, 9)
    n = str(n).replace("8", "5")

print(n)
