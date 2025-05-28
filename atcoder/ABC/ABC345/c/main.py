from collections import Counter

S = input().strip()
N = len(S)
count_dict = Counter(S)

# 交換可能な組み合わせ数
total_combinations = N * (N - 1) // 2

# 重複排除のために引くべき数
# 同じ文字を2つ選ぶ組み合わせ
duplicate_combinations = sum(count * (count - 1) // 2 for count in count_dict.values())

# 同じ文字が2回以上出現する場合、元の文字列がそのまま残る
same_string = 1 if duplicate_combinations >= 1 else 0

# 最終結果
result = total_combinations - duplicate_combinations + same_string
print(result)
