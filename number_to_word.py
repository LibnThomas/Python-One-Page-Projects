single={0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",}
ones={11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",10:"Ten",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",}
b=""
def convert(a):
	global b
	if(int(a/10000000)>=1):
		t=a%10000000
		a=int(a/10000000)
		if(single.get(a)==None):
			if(ones.get(a)==None):
				b=convert(a)
				b=b+" Crore "
				b=convert(t)
			else:
				b=b+ones[a]+" crore "
				b=convert(t)
		else:
			b=b+single[a]+" crore "
			b=convert(t)
	elif(int(a/100000)>=1):
		t=a%100000
		a=int(a/100000)
		if(single.get(a)==None):
			if(ones.get(a)==None):
				b=convert(a)
				b=b+" Lakh "
				b=convert(t)
			else:
				b=b+ones[a]+" Lakh "
				b=convert(t)
		else:
			b=b+single[a]+" Lakh "
			b=convert(t)
	elif(int(a/1000)>=1):
		t=a%1000
		a=int(a/1000)
		if(single.get(a)==None):
			if(ones.get(a)==None):
				b=convert(a)
				b=b+" Thousand "
				b=convert(t)
			else:
				b=b+ones[a]+" Thousand "
				b=convert(t)
		else:
			b=b+single[a]+" Thousand "
			b=convert(t)
	elif(int(a/100)>=1):
		t=a%100
		a=int(a/100)
		b=b+single[a]+" Hundred "
		if(t>=1):
			b=b+" and "
		b=convert(t)
	elif(int(a/10)>1):
		t=a%10
		a=a-t
		b=b+" "+ones[a]
		b=convert(t)
	elif(int(a/10)==1):
		b=b+" "+ones[a]
	else:
		a=a%10
		b=b+" "+single[a]
	return(b)
a=int(input(" Enter the Number : "))
print(convert(a))