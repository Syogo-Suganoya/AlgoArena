N = int(input())

# N を 2 進数で表現し、リストに格納
bits = bin(N)[2:]

# 結果を格納するリスト
result = []

# 各ビットに対して処理
for i, bit in enumerate(bits):
    if bit == "1":
        # 1 の位置に対応する魔法 A を追加
        result.append("A")
    # 魔法 B は 1 の後に追加
    if i != len(bits) - 1:
        result.append("B")

# 結果を文字列として返す
print("".join(result))
