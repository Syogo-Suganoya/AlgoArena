from collections import defaultdict

# N: 数列の長さ, M: 割る数
N, M = map(int, input().split())
A = list(map(int, input().split()))

# rem_counts[k][r]:
#   「a * 10^k % M == r となる a の個数」
# k = 連結される右側の数の桁数
rem_counts = [defaultdict(int) for _ in range(12)]

# 各 a について
# 「a を左側に置き、右側に k 桁の数が来る」場合の余りを前計算
for a in A:
    for k in range(1, 11):  # 桁数は最大 10 桁まで考えれば十分
        # a * 10^k を M で割った余り
        r = (a * pow(10, k, M)) % M
        rem_counts[k][r] += 1

ans = 0

# 今度は a を「右側の数」として固定して考える
for a in A:
    # a の桁数（連結時に使う）
    len_a = len(str(a))

    # a が右側に来たとき
    # 左側の数 x に対して
    #   x * 10^{len_a} + a ≡ 0 (mod M)
    # を満たす必要がある
    #
    # よって
    #   x * 10^{len_a} ≡ -a (mod M)
    #   x * 10^{len_a} % M == (M - a % M) % M
    target_rem = (M - (a % M)) % M

    # 条件を満たす左側の数の個数を加算
    ans += rem_counts[len_a][target_rem]

# 条件を満たす (左, 右) の組の総数を出力
print(ans)
