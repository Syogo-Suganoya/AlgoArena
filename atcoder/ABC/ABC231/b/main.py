from collections import defaultdict

N = int(input())
counter = defaultdict(int)

res = None
res_num = -1

for _ in range(N):
    S = input()
    counter[S] += 1  # カウントアップ

    # 登場回数が最大なら記録を更新
    if counter[S] > res_num:
        res = S
        res_num = counter[S]

print(res)
