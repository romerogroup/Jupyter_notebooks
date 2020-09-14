import sys
import sieve_ct

if __name__ == "__main__":
    
    if (len(sys.argv) > 1): 
        n = int(float(sys.argv[1]))
    else:
        n = 100
  
    print("")
    print(" Prime numbers up to %d" % n)
    nprimes = sieve_ct.SieveOfEratosthenes(n)
    print(" Function return: %d" % nprimes)
