f=2
i=2
def IsPrime(i, n):
	while i*i<=n and n%i!=0:
		i+=1
	return i*i>n

n=int(input())
while not IsPrime(i, f) or not IsPrime(i, n-f):
	f+=1
print(f, n-f)