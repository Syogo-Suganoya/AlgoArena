def main():
    n, _ = map(int, input().split())
    products = []

    # 各商品について、価格 p と機能集合 f を記録する
    for _ in range(n):
        data = list(map(int, input().split()))
        p = data[0]  # 価格
        _ = data[1]  # 機能数
        f = set(data[2:])  # 機能の集合（重複排除・高速な包含判定のために set を使用）
        products.append((p, f))

    # すべての商品の組み合わせ (i, j) について調べる（i ≠ j）
    for i in range(n):
        for j in range(n):
            if i == j:
                continue  # 同じ商品同士は比較しない

            pi, fi = products[i]  # 商品 i の価格と機能集合
            pj, fj = products[j]  # 商品 j の価格と機能集合

            # 条件1: 商品 j の方が安い or 同じ価格
            # 条件2: 商品 i の機能がすべて商品 j に含まれている（部分集合）
            if pj <= pi and fi.issubset(fj):
                # 条件3: より安い もしくは 機能が strictly more（真の上位集合）
                if pj < pi or fi != fj:
                    return True

    # どのペアでも上位互換が見つからなかった場合
    return False


print("Yes" if main() else "No")
