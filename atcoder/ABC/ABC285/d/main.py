"""
サイクルが見つかった場合は変更不可
サイクルがなければすべて変更可能
"""

from collections import defaultdict

n = int(input())
ad_list = {}  # ユーザーの変更関係を記録する辞書

# ユーザーの変更関係を入力として受け取る
for _ in range(n):
    s, t = input().split()
    ad_list[s] = t  # s から t への変更を記録

# メモ化用の辞書（既にサイクルが検出されたノードを記録）
memo = defaultdict(bool)

# 各ノード（ユーザー）の変更を探索
for k in ad_list.keys():
    t = k  # 開始ノード
    visited = set()  # 訪問したノードを記録するための集合

    # サイクル検出のためのループ
    while t in ad_list:
        if t in visited:  # 既に訪れたノードが現れた場合、サイクルが存在
            print("No")  # サイクルが存在するので変更不可能
            exit()  # プログラム終了

        visited.add(t)  # 訪問したノードとして記録

        # もしそのノードが既にサイクルのないノードなら探索を打ち切る
        if memo[t]:
            break

        # 次のノードに進む
        t = ad_list[t]

    # 訪問したノードをすべてサイクルがないとメモする
    for v in visited:
        memo[v] = True

# 全てのノードでサイクルが発見されなければ「Yes」を出力
print("Yes")
