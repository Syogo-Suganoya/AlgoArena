N, K = map(int, input().split())

S = input()

# はじめ、A でも B でもない文字で埋めておく
mp = {"C" * (K - 1): 1}

for c in S:
    # 末尾に 1 文字追加する
    # 'A' を追加する場合と 'B' を追加する場合を合併
    # 追加できない場合は空の dictionary で合併
    tmp = ({s + "A": v for s, v in mp.items()} if c != "B" else {}) | (
        {s + "B": v for s, v in mp.items()} if c != "A" else {}
    )

    mp = {}  # DP テーブルを消去

    for s, v in tmp.items():
        if s != s[::-1]:  # 回文でない場合、先頭を削って追加する
            if s[1:] in mp:
                mp[s[1:]] += v
            else:
                mp[s[1:]] = v

# 合計を 998244353 で割ったあまりが答え
print(sum(mp.values()) % 998244353)
