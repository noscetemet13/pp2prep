n=int(input())
watch=list()
for i in range(n):
	h,m,s=map(int, input().split())
	time=h*3600+m*60+s
	ok=True
	for i in range(0, len(watch)):
		if time<watch[i]:
			watch.insert(i, time)
			ok=False
			break
	if ok:
		watch.append(time)
for i in range(n):
	print(watch[i]//3600, watch[i]%3600//60, watch[i]%60)