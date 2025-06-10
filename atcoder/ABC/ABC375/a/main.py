N = int(input())
S = input()

res = 0

# 文字列 S の 0 から N-3 までをループ（3文字見るため、末尾2文字は対象外）
for i in range(N - 2):
    # 部分文字列 S[i:i+3] が "#.#" と一致するかをチェック
    if S[i : i + 3] == "#.#":
        res += 1

print(res)
