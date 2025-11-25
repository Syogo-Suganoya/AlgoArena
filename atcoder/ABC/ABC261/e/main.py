def bit(x, i):
    return (x >> i) & 1


n, c = map(int, input().split())
ops = [tuple(map(int, input().split())) for _ in range(n)]
ans = [0] * n

for k in range(30):
    func = [0, 1]  # 0 と 1 の状態
    crr = bit(c, k)

    for i, (op_type, x_val) in enumerate(ops):
        x = bit(x_val, k)
        if op_type == 1:  # AND
            f = [0 & x, 1 & x]
        elif op_type == 2:  # OR
            f = [0 | x, 1 | x]
        elif op_type == 3:  # XOR
            f = [0 ^ x, 1 ^ x]

        # func の更新
        func = [f[func[0]], f[func[1]]]
        crr = func[crr]
        ans[i] |= crr << k

for a in ans:
    print(a)
