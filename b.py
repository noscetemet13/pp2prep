n=int(input())
att={}
for i in range(n):
	name, date=input().split()
	if name in att:
		if date not in att[name]:
			att[name].append(date)
	else:
		att[name]=date
for i in att.keys():
	print(i, end=" ")
	if len(att[name])>=3:
		print("+1")
	else: print("NO BONUS")