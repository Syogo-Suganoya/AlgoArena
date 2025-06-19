N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

# 合宿開始前に準備されていたチョコレートの総数を計算
total = X  # 残りのチョコレートを加算
for a in A:
    # 各参加者が食べるチョコレートの数を計算
    eaten = (D - 1) // a + 1
    total += eaten

print(total)
