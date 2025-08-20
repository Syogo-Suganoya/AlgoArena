N = int(input())
A = list(map(int, input().split()))


ans = -sum(A)  # 後で調整するために最初に -sum(A) を入れておく

for p in range(30):  # 2^30 以上なのでこれくらいで十分
    # 運用中に累積 XOR が 0 か 1 かを数えていく
    count0 = 1  # 最初は累積 XOR = 0 を「1 回」カウント（初期の前提）
    count1 = 0
    x = 0
    for a in A:
        x ^= (a >> p) & 1  # p ビット目を取り出して累積 XOR
        if x == 0:
            count0 += 1
        else:
            count1 += 1
    ans += count0 * count1 * (1 << p)

print(ans)
