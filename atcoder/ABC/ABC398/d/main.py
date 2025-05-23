def main():
    _, R, C = map(int, input().split())
    S = input()

    f = [0, 0]  # 現在の焚き火の位置（初期は原点 (0,0)）
    st = set()  # 煙が発生した座標を管理する集合
    st.add((f[0], f[1]))  # 初期位置 (0,0) に煙があるので追加

    for nx in S:  # 各時刻ごとに風向きを処理
        # 風に逆らう形で焚き火と高橋君の位置を動かす
        if nx == "N":
            R += 1  # 高橋君を南に戻す → 座標的には北へ +1
            f[0] += 1  # 焚き火も北へ +1
        elif nx == "W":
            C += 1  # 高橋君を東に戻す → 座標的には西へ +1
            f[1] += 1  # 焚き火も西へ +1
        elif nx == "S":
            R -= 1  # 高橋君を北に戻す → 座標的には南へ -1
            f[0] -= 1  # 焚き火も南へ -1
        else:  # 'E'
            C -= 1  # 高橋君を西に戻す → 座標的には東へ -1
            f[1] -= 1  # 焚き火も東へ -1

        st.add((f[0], f[1]))  # 移動後の焚き火位置にも煙が発生するので記録

        # 高橋君の現在地に煙があるかを判定
        if (R, C) not in st:
            print(0, end="")  # 煙がなければ0
        else:
            print(1, end="")  # 煙があれば1
    print()  # 最後に改行


if __name__ == "__main__":
    main()
