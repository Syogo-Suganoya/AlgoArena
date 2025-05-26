from datetime import date

Y = int(input())
print((date(Y + 1, 1, 1) - date(Y, 1, 1)).days)
