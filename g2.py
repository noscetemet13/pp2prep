n=int(input())
watch=[]
fixed=[]
while n>0:
	h, m, s=map(int, input().split())
	time=h*3600+m*60+s
	watch.append(time)
	n-=1
while len(watch)>0:
	mn=watch[0]
	for i in watch:
		if i<mn:
			mn=i
	fixed.append(mn)
	watch.remove(mn)
while len(fixed)>0:
	hours=fixed[0]//3600
	minutes=(fixed[0]-hours*3600)//60
	seconds=fixed[0]-hours*3600-minutes*60
	print(hours, minutes, seconds)
	fixed.remove(fixed[0])