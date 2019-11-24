dic={}
a={"a":"z","b":"x","c":"c","d":"v","e":"b","f":"n","g":"m","h":"l","i":"k","j":"j","k":"h","l":"g","m":"f","n":"d","o":"s","p":"a","q":"p","r":"o","s":"i","t":"u","u":"y","v":"t","w":"r","x":"e","y":"w","z":"q"}
A={"A":"Z","B":"X","C":"C","D":"V","E":"B","F":"N","G":"M","H":"L","I":"K","J":"J","K":"H","L":"G","M":"F","N":"D","O":"S","P":"A","Q":"P","R":"O","S":"I","T":"U","U":"Y","V":"T","W":"R","X":"E","Y":"W","Z":"Q"}
dic=a
DIC=A

def iterate():
	temp=""
	for i,val in dic.items():
		if(i=="a"):
			temp=val
		elif(i=="z"):
			a[i]=temp
			a["a"]=val
		else:
			a[i]=temp
			temp=val

	temp=""
	for i,val in DIC.items():
		if(i=="A"):
			temp=val
		elif(i=="Z"):
			A[i]=temp
			A["A"]=val
		else:
			A[i]=temp
			temp=val
text="Ulb pykch xosrd nse jyfai stbo ulb gzqw vsm. Imv qzdyv ovfivfxv gqe hddj tvlpc zui li mvhso edu id ufhdxj imv tmdhv sqpqnpqsm. Zfgbawoijwomfgp. Nc tgo esx ewkx pg sxez pbx ubgkx fesevsefb fsgfxskt pbxh tgo beix aoqqxaacokkt zxqstfpxz pbx apsnhv wop lxxf np axqsxp ea ux uehp pg lhgu ubg ekk qgokz qseql pbx xhqstfpngh. Glzrsz whjarwa BZZZ SE WZWAL rlhjc ibav avz whqz yhp vroz pszq ah qzwdyga avz sadbjc rjq rlsh avz kzssrcz yhp cha rxazd qzwdygabhj"
ans,ec="",""
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