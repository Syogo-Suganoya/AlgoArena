import re

S = input().strip()

pattern = re.compile(r"^A[a-z]+C[a-z]+$")
if pattern.match(S):
    print("AC")
else:
    print("WA")
