n=int(input())
h=list(map(int, input().split()))
q=int(input())
def pillars(h, l, r):
	cnt=0
	mx=-1000000
	for i in range(l, r+1):
		if h[i]>mx:
			mx=h[i]
			cnt+=1
	print(cnt)
cnt=0
for i in range(q):
	l, r=map(int, input().split())
	pillars(h, l, r)