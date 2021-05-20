l, r=map(int, input().split())
def odd(l, r):
	if l%2==1: 
		print(l, end=" ")
	if l==r: return 0
	l=l+1
	return odd(l, r)
odd(l, r)