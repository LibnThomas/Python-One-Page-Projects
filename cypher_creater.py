a={"q":"z","w":"y","e":"x","r":"w","t":"v","y":"u","u":"t","i":"s","o":"r","p":"q","a":"p","s":"o","d":"n","f":"m","g":"l","h":"k","j":"j","k":"i","l":"h","m":"g","n":"f","b":"e","v":"d","c":"c","x":"b","z":"a"}
A={"Q":"Z","W":"Y","E":"X","R":"W","T":"V","Y":"U","U":"T","I":"S","O":"R","P":"Q","A":"P","S":"O","D":"N","F":"M","G":"L","H":"K","J":"J","K":"I","L":"H","M":"G","N":"F","B":"E","V":"D","C":"C","X":"B","Z":"A"}


dic=a
DIC=A

def iterate():
	temp=""
	for i,val in dic.items():
		if(i=="q"):
			temp=val
		elif(i=="z"):
			a[i]=temp
			a["q"]=val
		else:
			a[i]=temp
			temp=val

	temp=""
	for i,val in DIC.items():
		if(i=="Z"):
			temp=val
		elif(i=="A"):
			A[i]=temp
			A["Z"]=val
		else:
			A[i]=temp
			temp=val
# text="The quick brown fox jumps over the lazy dog. The above sentence may look weird but it helps you to unlock the whole paragraph. Congratulations. If you are able to read the whole paragraph properly then you have successfully decrypted the string but keep it secret as we want to know who all could crack the encryption. Please contact IEEE SB CECTL along with the code you have used to decrypt the string and also the message you got after decryption"
ans,ec="",""
text="Hello Ashly Congratulations for decryption This code"
enc=[]
for i in text:
	if(i!="."):
		ec=ec+i
	else:
		ec=ec+"."
		enc.append(ec)
		ec=""
enc.append(ec)
for i in enc:
	for l in i:
		for j,k in dic.items():
			flag=0
			if(l==k):
				ans=ans+j
			else:
				for x,y in DIC.items():
					if(l==y):
						ans=ans+x
						flag=1
			if(flag==1):
				break
		if(l==" "):
			ans=ans+" "
		if(l=="."):
			ans=ans+"."
	iterate()
print(ans)