class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 値→ノード の辞書
nodes = {}

# 番兵（ダミーノード）を作っておく
head = Node(None)
tail = Node(None)
head.next = tail
tail.prev = head

# 初期列を linked list に構築
cur = head
for a in A:
    node = Node(a)
    nodes[a] = node
    cur.next = node
    node.prev = cur
    cur = node
cur.next = tail
tail.prev = cur

# クエリ処理
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        x, y = int(q[1]), int(q[2])
        node_x = nodes[x]
        node_y = Node(y)
        nodes[y] = node_y
        nxt = node_x.next
        # 挿入
        node_x.next = node_y
        node_y.prev = node_x
        node_y.next = nxt
        nxt.prev = node_y
    else:  # "2 x"
        x = int(q[1])
        node_x = nodes[x]
        prv = node_x.prev
        nxt = node_x.next
        prv.next = nxt
        nxt.prev = prv
        del nodes[x]  # 辞書から削除

# 出力（headから順に辿る）
ans = []
cur = head.next
while cur != tail:
    ans.append(str(cur.val))
    cur = cur.next
print(" ".join(ans))
