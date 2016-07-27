import math
x=float(input("Enter value for x: "))
k=int(input("Enter value for k: "))
arctan=0.0
sign=1
ctr=1
for i in range(k):
	arctan=arctan+(sign*(x ** ctr)/ctr)
	ctr = ctr + 2
	sign = sign * -1
print(arctan)
print(math.atan(x))
