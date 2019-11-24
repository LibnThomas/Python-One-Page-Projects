set1=set()
set2=set()
set3=set()
a=int(input("Enter the Range of People Read Newspaper A :"))
for i in range(a):
	b=input("Enter the Name :")
	set1.add(b)
a=int(input("Enter the Range of People Read Newspaper B :"))
for i in range(a):
	b=input("Enter the Name :")
	set2.add(b)
a=int(input("Enter the Range of People Read Newspaper C :"))
for i in range(a):
	b=input("Enter the Name :")
	set3.add(b)

print(" People who read paper A 		: ",set1)
print(" People who read paper B 		: ",set2)
print(" People who read paper C 		: ",set3)

print(" People who read only paper A 		: ",set1-set2-set3)
print(" People who read only paper B 		: ",set2-set3-set1)
print(" People who read only paper C 		: ",set3-set2-set1)

print("\n People who read paper A and B 		: ",set1&set2)
print(" People who read paper B and C 		: ",set2&set3)
print(" People who read paper C and A 		: ",set3&set1)

print(" \nPeople who read paper A, B and C 	: ",set1&set2&set3)