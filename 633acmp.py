lines=[]
for i in range(4):
	line=input()
	lines.append(line)
lines[1:]=sorted(lines[1:])
print(lines[0]+": "+lines[1]+", "+lines[2]+", "+lines[3])