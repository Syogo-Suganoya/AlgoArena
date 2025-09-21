def to_base_minus2(n: int) -> str:
    if n == 0:
        return "0"
    res = ""
    while n != 0:
        # −2で割った余りを取る
        # Python の % 演算子で余りは「割る数」と同符号になるので調整する必要がある
        r = n % (-2)
        n = n // (-2)
        if r < 0:
            # 余りが負になるとき補正
            r += 2
            n += 1
        # r は 0 or 1 になる
        res = str(r) + res
    return res


N = int(input())
print(to_base_minus2(N))
