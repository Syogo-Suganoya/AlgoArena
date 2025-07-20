N = int(input())
s = set()

valid_suits = {"H", "D", "C", "S"}
valid_ranks = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}

for _ in range(N):
    card = input()
    suit, rank = card[0], card[1]
    # スート・ランクが不正ならNG
    if suit not in valid_suits or rank not in valid_ranks:
        print("No")
        break
    # 重複チェック
    if card in s:
        print("No")
        break
    s.add(card)
else:
    print("Yes")
