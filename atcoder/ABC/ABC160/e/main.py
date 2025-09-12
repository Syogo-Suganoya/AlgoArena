X, Y, A, B, C = map(int, input().split())
reds = sorted(list(map(int, input().split())), reverse=True)[:X]
greens = sorted(list(map(int, input().split())), reverse=True)[:Y]
colorless = list(map(int, input().split()))

# 上位X個の赤、上位Y個の緑、そして無色すべてを合体し、一番美味しい順に並べる
cand = reds + greens + colorless
cand.sort(reverse=True)

# その中から最初の X+Y 個を食べる
ans = sum(cand[: X + Y])
print(ans)
