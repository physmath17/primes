import math
import numpy as np

def prime_num(n):
	for i in range(2, int(math.sqrt(n)) + 1):
        	if n % i == 0:
        		return False
	return True	

c = 0	
prime = np.empty(10**6)

for i in range(2, 10**6):
	if prime_num(i) == True:
		prime[c] = i
		c = c + 1
	
print(c)
print(prime[0:100])
print(prime[9999])
print(prime_num(9973))

