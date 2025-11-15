N, Q = map(int, input().split())

# 各ノードの情報を [親ノードのインデックス, 親から追加された文字列] で管理
# nodes[0] は根ノード (空文字列)
nodes = [[None, ""]]  # 根ノード (インデックス 0)

# サーバーが指しているノードのインデックス
server_node_index = 0
# 各PC (0-indexed) が指しているノードのインデックス
pc_node_indices = [0] * N

for _ in range(Q):
    query = input().split()
    query_type = query[0]

    if query_type == "1":
        # クエリ1: PC p の文字列をサーバーの文字列で置き換える
        # PC p が指すノードを、サーバーが指すノードにする
        p = int(query[1]) - 1  # 0-indexed に
        pc_node_indices[p] = server_node_index

    elif query_type == "2":
        # クエリ2: PC p の文字列の末尾に s を追加する
        p = int(query[1]) - 1  # 0-indexed に
        s = query[2]

        # 現在のPC p が指すノードを親とする
        parent_index = pc_node_indices[p]
        # 新しいノードを作成
        new_node_index = len(nodes)
        nodes.append([parent_index, s])

        # PC p が指すノードを新しいノードに更新
        pc_node_indices[p] = new_node_index

    elif query_type == "3":
        # クエリ3: サーバーの文字列を PC p の文字列で置き換える
        p = int(query[1]) - 1  # 0-indexed に
        # サーバーが指すノードを、PC p が指すノードにする
        server_node_index = pc_node_indices[p]

# --- 全クエリ処理完了 ---

# 最終的にサーバーが指しているノードから根までたどり、文字列を復元
parts = []
current_index = server_node_index

# 根ノード (親が None) に達するまで親をたどる
while current_index is not None:
    parent_index, added_string = nodes[current_index]
    parts.append(added_string)  # 追加された文字列をリストに格納
    current_index = parent_index  # 親ノードへ移動

# 根からたどると parts = ["", "at", "coder"] のようになる
# 実際には ["coder", "at", ""] の順で集まるので、
# これを逆順 (reversed) にして連結 (join) する
final_server_string = "".join(reversed(parts))

print(final_server_string)
