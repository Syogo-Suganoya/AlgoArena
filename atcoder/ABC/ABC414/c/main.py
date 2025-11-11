def to_base(n: int, base: int) -> str:
    """整数nをbase進法の文字列に変換する"""
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return "".join(reversed(digits))


def is_palindrome(s: str) -> bool:
    """文字列sが回文かどうかを判定"""
    return s == s[::-1]


A = int(input())
N = int(input())

ans = 0

# 10進法の回文数を列挙
# 前半部分を作って、それを反転して後半に繋げる
for half in range(1, 10**6):  # 約6桁までで十分（N <= 10^12 を想定）
    s = str(half)

    # 奇数桁回文（例: 123 -> 12321）
    odd_pal = int(s + s[-2::-1])
    if odd_pal <= N:
        if is_palindrome(to_base(odd_pal, A)):
            ans += odd_pal

    # 偶数桁回文（例: 123 -> 123321）
    even_pal = int(s + s[::-1])
    if even_pal <= N:
        if is_palindrome(to_base(even_pal, A)):
            ans += even_pal

print(ans)
