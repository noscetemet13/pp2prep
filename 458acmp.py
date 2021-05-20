f=open("INPUT.TXT", "r")
a=f.readline()
b=f.readline()
c=a*b
f.close()
f2=open("OUTPUT.TXT", "w")
f2.write(c)
f2.close()