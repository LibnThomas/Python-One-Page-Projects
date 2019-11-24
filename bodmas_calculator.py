import math
a=input("Enter the Values : ")
li=('(',')','/','*','+','-')
val1=[]
bli=[]
b=""
for i in a:
	if(i in li):
		val1.append(b)
		val1.append(i)
		b=""
	else:
		b=b+i
val1.append(b)

def printval(val):
	g=""
	for i in val:
		g=g+str(i)
	print(g)

def cal(val):
	global li
	ii=0
	printval(val)
	for i in li:
		if(i in val):
			ii=val.index(i)
			if(i=="/"):
				s=float(val[ii-1])/float(val[ii+1])
				cal1(ii,round(s,4),val)
				break
			elif(i=="*"):
				s=float(val[ii-1])*float(val[ii+1])
				cal1(ii,round(s,4),val)
				break
			elif(i=="+"):
				s=float(val[ii-1])+float(val[ii+1])
				cal1(ii,round(s,4),val)
				break
			elif(i=="-"):
				s=float(val[ii-1])-float(val[ii+1]) 
				cal1(ii,round(s,4),val)
				break
	return val

def split(val):
	global bli
	ii=0
	while(len(val)!=1):
		for i in val:
			if(i=="("):
				c=0
				for i in val:
					if(i==")"):
						for i in range(ii+1,c):
							bli.append(val[i])
						bli=cal(bli)
						while(len(bli)!=1) :
							bli=cal(bli)
						del val[ii-1:c+2]
						val.insert(ii-1,bli[0])
						bli.clear()
						c=0
						break
					c+=1
			ii+=1
		val=cal(val)
	return(val)


def cal1(ii,s,val):
	print("Results :",val[ii-1],val[ii],val[ii+1],"=",s)
	del val[ii+1]
	del val[ii]
	del val[ii-1]
	val.insert(ii-1,s)
	return val

val=split(val1)

print("final result :",val[0])