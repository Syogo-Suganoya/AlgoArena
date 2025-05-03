from collections import defaultdict

N = int(input())  # 要素数
A = list(map(int, input().split()))  # 値A（重複あり）
W = list(map(int, input().split()))  # 値Aに対応する重みW

# 値Aごとに対応するWをまとめる
groups = defaultdict(list)
for a, w in zip(A, W, strict=True):
    groups[a].append(w)

res = 0

# 各値Aに対応するWが複数あるもの（重複しているA）だけ処理
for key, w_list in groups.items():
    # 重複だけ処理
    if len(w_list) <= 1:
        continue
    w_list.sort()
    # 最小値のうち、(個数 - 1)個ぶん足す
    tmp = sum(w_list[: len(w_list) - 1])
    res += tmp

print(res)
