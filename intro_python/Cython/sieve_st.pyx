#cython: language_level=3, boundscheck=False

import sys

def SieveOfEratosthenes(n):

    cdef int imax, neff, p, i, counter, nprimes

    if n%2 == 0:
        imax=int(n/2)
    else:
        imax=int((n+1)/2)

    neff= 2*(imax-1)+1
    prime = imax*[True]

    print(" Dimension of array: %d\n" % imax)
    print(" Array with indices between 0 to %d\n" % (imax-1))
    print(" Stores primality of odd numbers in range [1, %d]\n\n" % neff)

    # The loop runs over all odd numbers starting at 3
    p=3
    while (p<n/2+1):
        # If prime[p] is true, then it is a prime
        if(prime[int((p-1)/2)] == 1):
            # Update all multiples of p
            i = 2*p
            while (i <= neff):
                if (i%2!=0):
                    prime[int((i-1)/2)] = False
                i += p
        p+=2
        
    counter = 1
    nprimes = 0
    # Print all prime numbers if the number is small otherwise just count the number of primes found
    if (imax < 10000):
        print("%10d " % 2, end='')
        # Starting with index 1 instead of zero because (2*0)+1 = 1 is not prime
        for i in range(1,imax):
            if(prime[i] == 1):
                print("%10d " % (2*i+1), end='')
                counter+=1
          
            if (counter == 15):
                print("")
                counter=0
          
        print("\n")
        
    else:
        for i in range(1,imax):
            if(prime[i] is True):
                nprimes+=1
        print(" Total number of primes found: %d" % nprimes)
      
    return nprimes

