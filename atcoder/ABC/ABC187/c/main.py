N = int(input())

# 2つの集合を用意
normal_set = set()  # ついていないもの
negated_set = set()  # ついているもの（先頭の!を除いた形で入れる）

for _ in range(N):
    S = input()
    if S.startswith("!"):
        negated_set.add(S[1:])  # 除いて追加
    else:
        normal_set.add(S)

# どちらにも存在する語があるかを探索
for word in normal_set:
    if word in negated_set:
        print(word)
        break
else:
    print("satisfiable")
