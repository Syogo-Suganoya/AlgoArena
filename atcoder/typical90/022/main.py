A, B, C = map(int, input().split())


# ユークリッドの互除法による最大公約数 (gcd) の計算
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# gcdを計算
S = gcd(A, gcd(B, C))

# 結果を計算して出力
result = (A // S - 1) + (B // S - 1) + (C // S - 1)
print(result)
