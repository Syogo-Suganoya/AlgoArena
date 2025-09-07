import sys

sys.setrecursionlimit(10**7)

S = input().strip()
Q = int(input())


# 'A'=0, 'B'=1, 'C'=2 として数値に変換すると計算が楽になる
def char_to_int(c):
    return ord(c) - ord("A")


def int_to_char(x):
    return chr(x + ord("A"))


# f(t, k, c):
#   文字 c (0=A,1=B,2=C) を t 回変換したときに
#   k 番目(1-indexed) の文字が何になるかを返す
def f(t, k, c):
    if t == 0:
        return c
    if k == 1:
        # 左端は単純に t 回だけ (A->B->C->A...) と回転する
        return (c + t) % 3
    # 再帰的に一つ上の段階へ
    parent = f(t - 1, (k + 1) // 2, c)
    # k の偶奇で左右を判定
    if k % 2 == 1:  # 左側の子
        return (parent + 1) % 3
    else:  # 右側の子
        return (parent + 2) % 3


for _ in range(Q):
    t, k = map(int, input().split())
    # S の (kを遡っていった先の文字) が元になる
    # 実際は元の文字列 S の (kを2進的に遡って) 対応する文字をとる必要がある
    # → floor((k-1) >> t) の位置が元のインデックスになる
    base_index = (k - 1) >> t
    c = char_to_int(S[base_index])

    ans = f(t, k, c)
    print(int_to_char(ans))
