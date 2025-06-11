H = int(input())  # 超えたい高さを入力

day = 0  # 何日経ったか
height = 0  # 現在の植物の高さ

# 毎晩 2^day cm ずつ成長する
# 朝の時点で H を超えた最初の日を探す
while height <= H:
    height += 2**day  # 今日の夜の成長分を足す
    day += 1  # 次の日へ

# 初めて H を超えた日の朝
print(day)
