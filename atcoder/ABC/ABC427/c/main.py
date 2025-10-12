N, M = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]

ans = M
# 2^N 通りの塗り方を全部探索する
for bit in range(2**N):
    delete_count = 0
    for u, v in edges:  # それぞれの辺を見て
        if (1 & (bit >> u)) == (
            1 & (bit >> v)
        ):  # 結んでいる頂点が同じ色で塗られていたら
            delete_count += 1  # カウントを増やす
    ans = min(ans, delete_count)

print(ans)
