S, T, X = map(int, input().split())

# S > T のときは日をまたぐので、TとXに+24して日付をまたがせて調整
if S > T:
    T += 24
    if X < S:
        X += 24

# 起床時刻 S <= X < 就寝時刻 T の範囲にXがあるかどうか
if S <= X < T:
    print("Yes")
else:
    print("No")
