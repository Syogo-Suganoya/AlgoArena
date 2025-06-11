N, M, K = map(int, input().split())
tests = []
results = []
for _ in range(M):
    *keys, r = input().split()
    c = int(keys[0])  # 使った鍵の本数
    arr = list(map(int, keys[1:]))
    mask = 0
    for x in arr:
        mask |= 1 << (x - 1)
    tests.append(mask)
    results.append(r == "o")

ans = 0
for bit in range(1 << N):
    ok = True
    for i in range(M):
        cnt = bin(bit & tests[i]).count("1")
        if (cnt >= K) != results[i]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
