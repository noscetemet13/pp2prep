n, k=map(int, input().split())
newn=""
while n>0:
	newn=newn+str(n%k)
	n//=k
p=1
s=0
for i in range(len(newn)):
	p*=int(newn[i])
	s+=int(newn[i])
print(p-s)