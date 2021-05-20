s=input()
d={}
for i in s:
	d[i]=d.get(i, 0)+1
cnt=0
for i in d.values():
	if i%2==1:
		cnt+=1
if len(s)==0: print("ZA WARUDO TOKI WO TOMARE")
elif cnt<=1: print("ZA WARUDO TOKI WO TOMARE")
else: print("JOJO")