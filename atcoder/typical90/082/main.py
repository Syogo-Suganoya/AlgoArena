def count_total_characters(L, R):
    MOD = 10**9 + 7
    total_characters = 0
    current = L

    while current <= R:
        # current の桁数を求める
        current_length = len(str(current))
        # current_length 桁の最大値
        max_in_this_length = 10**current_length - 1
        # この桁数での範囲の終わり
        end = min(R, max_in_this_length)
        # この範囲の数の個数
        count = end - current + 1
        print(current_length, max_in_this_length, end)
        # 文字数の総和を計算
        total_characters += current_length * (count * (current + end) // 2)
        total_characters %= MOD
        # 次の桁数へ
        current = end + 1

    return total_characters


# 入力の読み込み
L, R = map(int, input().split())
# 結果の出力
print(count_total_characters(L, R))
