N, K = map(int, input().split())
S = input()

# 初期状態での幸福な箇所（隣り合う文字が同じ）を数える
happy = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        happy += 1

# 操作で最大 2*K 箇所の幸福を増やせるが、幸福な箇所の最大数は N-1
# 最終的な幸福な箇所の数は happy + 2*K を N-1 でクリップする
print(min(happy + 2 * K, N - 1))
