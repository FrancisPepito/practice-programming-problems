arr=[]
for i in range(int(input("Enter an integer: "))):
	arr.append(input("Enter string: "))
for i in range(int(input("Enter an integer: "))):
	l=int(input("L: "))
	r=int(input("R: "))
	sub=input("String: ")
	check=0
	for i in range(l-1,r):
		if(sub==arr[i]):
			check = check + 1
	print(check)
