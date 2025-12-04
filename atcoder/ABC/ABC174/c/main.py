K = int(input())

rem = 7 % K  # 最初の項 7 の剰余
i = 1  # 項番号

while rem != 0 and i < K:
    rem = (rem * 10 + 7) % K  # 次の項の剰余
    i += 1

if rem == 0:
    print(i)  # 剰余が0になった時の項番号を出力
else:
    print(-1)  # K の倍数になる項がない場合
