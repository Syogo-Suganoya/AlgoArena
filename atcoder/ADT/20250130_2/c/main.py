from datetime import datetime, timedelta

H, M = map(int, input().split())


def main():
    hh = H
    mm = M
    while True:
        str_h = str(hh).zfill(2)
        str_m = str(mm).zfill(2)
        othre_h = int(str_h[0] + str_m[0])
        othre_m = int(str_h[1] + str_m[1])
        if 0 <= othre_h <= 23 and 0 <= othre_m <= 59:
            return int(str_h), int(str_m)
        time = datetime.strptime(f"{hh}:{mm}", "%H:%M")
        new_time = time + timedelta(minutes=1)
        hh, mm = new_time.strftime("%H:%M").split(":")


print(*main())
