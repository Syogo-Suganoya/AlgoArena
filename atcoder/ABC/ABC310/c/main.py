n = int(input())
unique_strings = set()

for _ in range(n):
    s = input()
    reversed_s = s[::-1]
    representative = min(s, reversed_s)  # 辞書順で小さい方を選ぶ
    unique_strings.add(representative)

print(len(unique_strings))
