N, K, X = map(int, input().split())
A = list(map(int, input().split()))

# 1. 高い順にソートして、クーポンをなるべく高いものに使う
A = sorted(A, reverse=True)

# 2. 各要素に対して、できるだけクーポンを使って値引き
for i in range(N):
    q = A[i] // X  # この商品に対して使える最大クーポン枚数
    use = min(q, K)  # 実際に使うクーポン枚数（Kが足りない場合もあるので）
    A[i] -= use * X  # クーポン分値引き
    K -= use  # 残りのクーポンを減らす
    if K == 0:
        break  # クーポン使い切ったら終了

# 3. もう一度高い順にソートして、残ったKをそのまま0円処理に使う
A = sorted(A, reverse=True)
ans = 0
for i in range(N):
    if K > 0:
        K -= 1
        continue  # この商品は無料
    ans += A[i]  # 残りの商品を加算
print(ans)
