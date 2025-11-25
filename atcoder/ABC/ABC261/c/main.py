N = int(input())
S = [input().strip() for _ in range(N)]

# 今までに出てきた文字列のカウントを辞書で管理
cnt = dict()

for s in S:
    if s not in cnt:
        # 初めて出てきた場合はそのまま出力
        print(s)
        cnt[s] = 1
    else:
        # すでに出ていた場合は (回数) をつけて出力
        print(f"{s}({cnt[s]})")
        cnt[s] += 1
