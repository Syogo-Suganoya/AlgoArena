MOD = 998244353


def count_set_bits(n, j):
    block_size = 1 << (j + 1)
    full_blocks = n // block_size
    remainder = n % block_size
    count = full_blocks * (1 << j)
    if remainder >= (1 << j):
        count += remainder - (1 << j) + 1
    return count


def masked_popcount():
    result = 0
    for j in range(60):
        if M & (1 << j):
            result += count_set_bits(N, j)
            result %= MOD
    return result


# 入力の読み込み
N, M = map(int, input().split())
print(masked_popcount())
