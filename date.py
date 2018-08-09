first = input()
#print(first)
second=first.split(",")
second=list(map(int,second))
#print(second)

third=list()
fourth=list()
fifth=list()
sixth=list()
seventh=list()
eight=list()
nine=list()
ten=list()

if 1 in second:
	position=second.index(1)
        #print(position)
	out='1'
	second.pop(position)
	third=second
	
	if 2 in third:
		position=third.index(2)
		out=out+'2/'
		third.pop(position)
		fourth=third
	
	elif 1 in third:
		position=third.index(1)
		out=out+'1/'
		third.pop(position)
		fourth=third
	
	elif 0 in third:
		position=third.index(0)
		out=out+'0/'
		third.pop(position)
		fourth=third

elif 0 in second:
	position=second.index(0)
	second.pop(position)
	third=second
	out='0'
	
	for i in (9,8,7,6,5,4,3,2,1):
		if i in third:
			position=third.index(i)
			out=out+str(i)+"/"
			third.pop(position)
			fourth=third
			break	

else:
	print(0)
	exit()

#print(out)

for i in (3,2,1,0):
	if i in fourth:
		position=fourth.index(i)
		out=out+str(i)
		fourth.pop(position)
		fifth=fourth
		break
#print(out)		
for i in (0,9,8,7,6,5,4,3,2,1):
	if i in fifth:
		position=fifth.index(i)
		out=out+str(i)+" "
		fifth.pop(position)
		sixth=fifth
		break

#print(out)

for i in (2,1,0):
	if i in sixth:
		position=sixth.index(i)
		out=out+str(i)
		sixth.pop(position)
		seventh=sixth
		break
#print(out)
#print(seventh)
#print(out[-1])
if out[-1]=='2':
	for i in (3,2,1,0):
		if i in seventh:
			position=seventh.index(i)
			out=out+str(i)+":"
			seventh.pop(position)
			eight=seventh
			break
else:
	for i in (9,8,7,6,5,4,3,2,1,0):
		if i in seventh:
			position=seventh.index(i)
			out=out+str(i)+":"
			seventh.pop(position)
			eight=seventh
			break
#print(out)

for i in (5,4,3,2,1):
	if i in eight:
		position=eight.index(i)
		out=out+str(i)
		eight.pop(position)
		nine=eight
		break

for i in (9,8,7,6,5,4,3,2,1,0):
	if i in nine:
		position=nine.index(i)
		out=out+str(i)
		nine.pop(position)
		ten=nine
		break

print(out)
