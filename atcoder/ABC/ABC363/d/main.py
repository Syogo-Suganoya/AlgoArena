N = int(input())

# Nが1から10までなら、0から9までの1桁の回文数の範囲
if N <= 10:
    print(N - 1)
    exit()  # 1番目は0、2番目は1、…となる

count = 10  # ここまでに存在する回文数の個数（1桁分をカウント）
digit = 2  # 現在の桁数（2桁以上を考えるため初期値は2）

while True:
    half_len = (digit + 1) // 2  # 回文を作るための前半の桁数
    start = 10 ** (half_len - 1)  # 前半部分の最小値（例：100...）
    end = 10**half_len - 1  # 前半部分の最大値（例：999...）
    num_palindromes = end - start + 1  # この桁数の回文数の個数

    # Nがこの桁数の回文数に含まれるかチェック
    if N <= count + num_palindromes:
        offset = N - count - 1  # この桁数内で何番目かを計算
        half_number = start + offset  # 前半部分の数字を決定
        half_str = str(half_number)  # 文字列に変換

        # 回文を作る
        if digit % 2 == 0:
            # 偶数桁の場合は前半をそのまま反転して後半に使う
            palindrome = half_str + half_str[::-1]
        else:
            # 奇数桁の場合は中央の数字を重複させずに反転して後半に使う
            palindrome = half_str + half_str[-2::-1]

        print(palindrome)
        break

    # Nがこの桁数に含まれない場合は次の桁数に進む
    count += num_palindromes
    digit += 1
