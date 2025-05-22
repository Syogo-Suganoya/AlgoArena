# 入力の読み込み
n = int(input())  # 町の数（使わないけど一応読む）
a, b = map(int, input().split())  # 出発地 a と 到着地 b
k = int(input())  # 経由する町の数
p = list(map(int, input().split()))  # 経由する町のリスト

# 経由地リストに出発地や到着地が含まれていないかチェック
if a in p or b in p:
    print("NO")  # 出発地または到着地が経由地に含まれていたらアウト
# 経由地に重複があるかをチェック（集合にして長さ比較）
elif len(set(p)) < len(p):
    print("NO")  # 同じ町を2回以上通っているので最短経路ではない
else:
    print("YES")  # 上記の条件を全て満たしていれば「最短経路の可能性あり」
