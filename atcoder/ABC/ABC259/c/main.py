from itertools import groupby

S = input()
T = input()


def run_length(s):
    """
    ランレングス圧縮: 連続する文字を (文字, 連続数) のタプルで表現する
    例: 'aaabb' → [('a', 3), ('b', 2)]
    """
    return [(k, len(list(g))) for k, g in groupby(s)]


rs = run_length(S)
rt = run_length(T)

if len(rs) != len(rt):
    print("No")
    exit()

for (cs, ns), (ct, nt) in zip(rs, rt, strict=True):
    if cs != ct:
        print("No")
        exit()
    if ns > nt:
        print("No")
        exit()
    if ns == 1 and nt >= 2:
        print("No")
        exit()

print("Yes")
