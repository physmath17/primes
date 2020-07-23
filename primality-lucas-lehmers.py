import math

val = input("Enter the number to be verified:")
n = int(val)

def lucas_lehmers(m):
	if m==0:
		return 4
	else:
		return (lucas_lehmers(m-1)**2 - 2)
	
power = int(math.log(n+1,2))
# print(power)

r = lucas_lehmers(0) % n

for i in range(1, power-1):
	print(r)
	s = (r**2 - 2) % n
	r = s
print(r)

if (r == 0):
	print(n, "is a prime")
else:
	print(n, "is not a prime")

