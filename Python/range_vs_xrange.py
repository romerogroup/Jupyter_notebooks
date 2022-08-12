#!/usr/bin/env python

import timeit

def test_range(n):
    sum=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ijk=i+j*k
                sum=sum+ ijk
                
                if ijk > 1:
                    break

            else:
                # Continue if the inner loop wasn't broken.
                continue
            # Inner loop was broken, break the outer.
            break

        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break


    return sum
            
def test_xrange(n):
    sum=0
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                ijk=i+j*k
                sum=sum+ ijk
                
                if ijk > 1:
                    break

            else:
                # Continue if the inner loop wasn't broken.
                continue
            # Inner loop was broken, break the outer.
            break

        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break

    return sum

if __name__ == '__main__':

    n = 2000000
    
    print("Using range() function:")
    print(timeit.timeit('test_range('+str(n)+')', setup="from __main__ import test_range", number=5))
    
    print("Using xrange() function:")
    print(timeit.timeit('test_xrange('+str(n)+')', setup="from __main__ import test_xrange", number=5))
