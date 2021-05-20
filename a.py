n=int(input())
m=int(input())
k=int(input())
maxi=max(n, m)
ok=False
for i in range(1, maxi):
	if i*m==k:
		print("YES")
		ok=True
		break
	if i*n==k:
		print("YES")
		ok=True
		break
if ok==False: print("NO")