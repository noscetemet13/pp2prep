f=open("INPUT.TXT", "r")
a=int(f.readline())
b=int(f.readline())
f.close()
f2=open("OUTPUT.TXT", "w")
c=a*b
f2.write(str(c))
f2.close()