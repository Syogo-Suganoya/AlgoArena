from datetime import datetime, timedelta

K = int(input())
t = datetime.strptime("21:00", "%H:%M")
t_plus = t + timedelta(minutes=K)
print(t_plus.strftime("%H:%M"))
