import math

val = input("Enter the number to be verified:")
n = int(val)

def SieveOfEratosthenes(m):

    # create a boolean array upto m+1 with all entries true, if a number l is not prime prime[l] will be false

    prime = [True for i in range(m+1)]
    
    p = 2
    while(p*p <= m):

        # if prime[p] is not changed it is a prime
        if(prime[p] == True):
            # update all multiples of p
            for i in range(p*p, m+1, p):
                prime[i] = False

        p += 1
    # printing primes
    #for i in range(2, n):
    if(prime[m] == True):
        print("prime")
    else:
        print("not a prime")

SieveOfEratosthenes(n)