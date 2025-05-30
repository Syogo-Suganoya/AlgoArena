N = int(input())

# N以上の数を919まで順に確認する
for i in range(N, 920):  # 919を含めるために920まで
    # iを各桁に分解
    digits = list(map(int, str(i)))
    # 1桁目と2桁目の積が3桁目と等しいか確認
    if digits[0] * digits[1] == digits[2]:
        print(i)
        break  # 条件を満たす最小のiを見つけたら終了
