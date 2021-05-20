a, b=map(int, input().split())
c, d=map(int, input().split())
if a+d>c+b:
	print("Barsenal")
	print(a+d, c+b)
elif a+d<c+b:
	print("Arselona")
	print(a+d, c+b)
elif a+d==c+b:
	if b>d:
		print("Arselona")
		print(a+d, c+b)
	elif d>b:
		print("Barsenal")
		print(a+d, c+b)
	else:
		print("Friendship")
		print(a+d, c+b)