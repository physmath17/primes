def lucas_lehmers(n):
	if n==0:
		return 4
	else:
		return (lucas_lehmers(n-1)**2 - 2)

for i in range(0,10):
	print(lucas_lehmers(i))
