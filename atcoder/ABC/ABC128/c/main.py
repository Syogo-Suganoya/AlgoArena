# 入力
N, M = map(int, input().split())
S = []
for _ in range(M):
    k, *lst = map(int, input().split())
    # 0-indexed に変換
    S.append([s - 1 for s in lst])
P = list(map(int, input().split()))

ans = 0
# 全てのスイッチのON/OFFパターンをビット全探索
for msk in range(1 << N):
    ok = 0
    for m in range(M):
        cnt = 0
        for s in S[m]:
            if msk & (1 << s):
                cnt += 1
        if cnt % 2 == P[m]:
            ok += 1
    if ok == M:
        ans += 1

print(ans)
