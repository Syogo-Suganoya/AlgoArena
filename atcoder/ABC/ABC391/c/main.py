# 公式解説から引用
# https://atcoder.jp/contests/abc391/editorial/12084

N, Q = map(int, input().split())

res = 0
cnt = [0] + [1] * N
pos = list(range(N + 1))

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            P, H = query[1:]
            # 鳩 P は移動する前は巣 pos[P] にいる
            # 鳩 P が移動することで 巣 pos[P] にいる鳩の数が 2 から 1 に減る場合, ans を 1 減らす
            if cnt[pos[P]] == 2:
                res -= 1
            # 巣 pos[P] の鳩の数を 1 減らす
            cnt[pos[P]] -= 1
            # 鳩 P がいる巣を H に変更する
            pos[P] = H
            # 巣 H の鳩の数を 1 増やす
            cnt[pos[P]] += 1
            # 鳩 P が移動することで 巣 H にいる鳩の数が 1 から 2 に増える場合，ans を 1 増やす
            if cnt[pos[P]] == 2:
                res += 1
        case 2:
            print(res)
