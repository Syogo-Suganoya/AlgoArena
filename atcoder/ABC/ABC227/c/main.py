N = int(input())
ans = 0

# A を 1 から順に決めていく
for a in range(1, N + 1):
    # A が大きすぎると、最小でも A^3 > N になって不可能
    if a * a * a > N:
        break

    # B を A から順に決めていく（A <= B <= C の条件を満たすため）
    for b in range(a, N + 1):
        # A * B が大きすぎると、最小の C=B でも A*B*B > N となり不可能
        if a * b * b > N:
            break

        # A, B が決まったとき、C の最大値は floor(N / (A*B))
        # ただし C >= B なので、範囲は [B, N//(A*B)]
        # 個数は N//(A*B) - B + 1
        ans += N // a // b - b + 1

# 答えを出力
print(ans)
