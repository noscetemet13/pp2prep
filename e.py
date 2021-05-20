import re
email=input()
ok=re.search(r"^[a-z]+@[a-z]+\.[a-z]+", email)
if ok: print("Yes")
else: print("No")