n, v, k=map(int, input().split())
b=0
pustoi=False
for i in range(n):
	b+=v
	v-=k
	if v<=0 and i!=n-1:
		pustoi=True
		break
	elif v<=0:
		pustoi=False
		break
if pustoi: print("NO "+str(b))
else: print("YES "+str(b))