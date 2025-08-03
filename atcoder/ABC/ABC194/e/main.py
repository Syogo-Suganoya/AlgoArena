# 入力の受け取り
n, m = map(int, input().split())  # n: 数列の長さ, m: 区間の長さ
nums = list(map(int, input().split()))  # 数列の内容

# 各値が最後に登場したインデックスを記録するリスト（初期値は -1：未出現）
last_seen_pos = [-1] * (n + 1)

# 各値について、「長さmのどの区間にも登場しなかった可能性があるか」を記録するフラグ
valid = [False] * (n + 1)

# 数列を先頭から見ていき、長さm以上空いていた場合は「登場しなかった可能性あり」とする
for i in range(n):
    # 前回登場した位置から現在位置までの間隔がmより大きい場合、
    # 間に長さmの区間が存在するので「そこに現れていない」可能性がある
    if i - last_seen_pos[nums[i]] > m:
        valid[nums[i]] = True
    # 現在の位置を最後に登場した位置として記録
    last_seen_pos[nums[i]] = i

# 数列の末尾以降にも長さmの区間が存在する可能性があるため、末尾部分もチェック
for i in range(n + 1):
    # 最後に登場した位置からnまでの間隔がmより大きければ、
    # 終端に含まれない長さmの区間が存在するため、「登場していない可能性あり」
    if n - last_seen_pos[i] > m:
        valid[i] = True

# 最小の「valid=True」となっている数値（＝m区間すべてに現れなかった最小値）を出力
for i in range(n + 1):
    if valid[i]:
        print(i)
        break
