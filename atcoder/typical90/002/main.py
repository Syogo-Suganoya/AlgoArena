N = int(input())


# 括弧列が正しいかを判定する関数
def is_valid(sequence):
    depth = 0
    for char in sequence:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        # 深さが負になった場合、正しくない括弧列
        if depth < 0:
            return False
    # 最終的に深さが0なら正しい括弧列
    return depth == 0


# メイン部分
def generate_brackets(N):
    # 2^N 通りを全探索
    for i in range(1 << N):
        candidate = ""
        for j in range(N - 1, -1, -1):  # 上位ビットから順に処理
            if (i & (1 << j)) == 0:
                candidate += "("
            else:
                candidate += ")"
        # 候補が正しい括弧列か判定
        if is_valid(candidate):
            print(candidate)


# 入力を受け取る
generate_brackets(N)
