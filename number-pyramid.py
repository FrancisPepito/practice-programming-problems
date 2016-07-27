a=''
ans=0
for i in range(1,10):
	a=a+str(i)
	ans=10**i + ans
	print(a,'=',str(ans-int(a)))
