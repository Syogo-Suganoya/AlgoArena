N = int(input())

# N の桁数
length = len(str(N))

# 3 桁以下ならそのまま出力
if length <= 3:
    print(N)
else:
    # 頭 3 桁を残し、残りは 0 にする
    head = str(N)[:3]
    zero_count = length - 3
    result = head + "0" * zero_count
    print(result)
