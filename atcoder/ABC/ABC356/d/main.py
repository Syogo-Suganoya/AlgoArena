N, M = map(int, input().split())
ans = 0
for bit in range(60):
    mask = 1 << bit
    if not (M & mask):
        continue  # M のそのビットが 0 のときは寄与しない

    # 「1 が立つ数 k の回数」を数えるロジック
    # N+1 個の数を、長さ mask*2 の周期で区切って考える

    full = (N + 1) // (mask * 2)  # 完全周期の数
    rem = (N + 1) % (mask * 2)  # 余りの長さ

    cnt = full * mask
    cnt += max(0, rem - mask)

    ans = (ans + cnt) % 998244353

print(ans)
