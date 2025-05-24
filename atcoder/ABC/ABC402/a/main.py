S = input()
import re

# 大文字の正規表現: [A-Z]+
upper_letters = re.findall(r"[A-Z]", S)
print("".join(upper_letters))
