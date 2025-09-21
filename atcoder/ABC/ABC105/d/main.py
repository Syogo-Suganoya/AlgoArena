from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

count_mod = defaultdict(int)
count_mod[0] = 1  # S_0 のあまり 0 を 1 回含めておく

sum_so_far = 0
answer = 0

for x in A:
    sum_so_far = (sum_so_far + x) % M
    # この時点で sum_so_far を S_i mod M とする
    # もしこのあまりが以前にも出ていたら、
    # その「以前のすべての位置 l-1」について、
    # ここを r とする区間 (l, r) が条件を満たす
    answer += count_mod[sum_so_far]
    # 今回のあまりを記録
    count_mod[sum_so_far] += 1

print(answer)
