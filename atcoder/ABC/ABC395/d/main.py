def main():
    N, Q = map(int, input().split())

    # 各巣に現在どのラベル鳩がいるかを管理するリスト
    box_to_label = list(range(N))  # box_to_label[i] = i番目の巣にいるラベル番号

    # 各ラベル鳩がどの巣にいるかを管理するリスト
    label_to_box = list(range(N))  # label_to_box[i] = ラベルiの鳩がいる巣番号

    # 各鳩（個体）がどの巣にいるかを管理するリスト
    pigeon_to_box = list(range(N))  # pigeon_to_box[i] = 鳩iがいる巣番号

    for _ in range(Q):
        op = list(map(int, input().split()))
        match op[0]:
            case 1:
                # 操作1: 鳩aをラベルbが付いた巣へ移動させる
                a = op[1]
                b = op[2]
                # 鳩aの現在位置を、ラベルbが付いている巣の場所に更新
                pigeon_to_box[a - 1] = label_to_box[b - 1]

            case 2:
                # 操作2: ラベルaとラベルbを交換する
                a = op[1]
                b = op[2]
                # まず、ラベルaとラベルbが付いている巣を入れ替える
                label_to_box[a - 1], label_to_box[b - 1] = (
                    label_to_box[b - 1],
                    label_to_box[a - 1],
                )

                # 次に、巣側が持っている「今どのラベル鳩がいるか」の情報も入れ替える
                (
                    box_to_label[label_to_box[a - 1]],
                    box_to_label[label_to_box[b - 1]],
                ) = (
                    box_to_label[label_to_box[b - 1]],
                    box_to_label[label_to_box[a - 1]],
                )
                # ※ここでは鳩自身は動かさない。巣に貼ってある「ラベル」だけを入れ替えるイメージ！

            case 3:
                # 操作3: 鳩aがいる巣のラベルを出力する
                a = op[1]
                # 鳩aが今いる巣(pigeon_to_box[a-1])のラベルを取り出して+1（0-index補正）
                print(box_to_label[pigeon_to_box[a - 1]] + 1)


def incorrect():
    """
    不正解な例

    removeやaddは、時間効率が悪い
    """
    N, Q = map(int, input().split())

    nests = [[i] for i in range(N)]
    pisions = list(range(N))

    for i in range(Q):
        op = list(map(int, input().split()))
        match op[0]:
            case 1:
                # 鳩a を、巣b へ移動する
                a = op[1] - 1
                b = op[2] - 1
                nests[pisions[a]].remove(a)
                pisions[a] = b
                nests[b].append(a)
            case 2:
                # 巣a と巣b を交換する
                a = op[1] - 1
                b = op[2] - 1

                for ai in nests[a]:
                    pisions[ai] = b
                for bi in nests[b]:
                    pisions[bi] = a

                nests[a], nests[b] = nests[b], nests[a]

            case 3:
                # 鳩a がいる巣 の番号を出力する
                a = op[1] - 1
                print(pisions[a] + 1)


if __name__ == "__main__":
    main()
