#!/usr/bin/env python3 

import argparse

class MultDivClass:

    def __init__(self, a=0, b=0):
       self.a = a
       self.b = b
       
    def run(self):
        self._private_product()
        self._private_division()
        
    # --- private
    def _private_product(self):
        print("The product of %f and %f is %f" % (self.a,self.b,self.a*self.b))
            
    def _private_division(self):
        if self.b == 0:
            print("Division by zero!")
        else:
            print("The division of %f by %f is %f" % (self.a,self.b,self.a/self.b))
            


if __name__ == "__main__":
    """
    Command line usage:
    `python -m path.to.my_file -a 12 -b 23` 
    """

    parser = argparse.ArgumentParser(description="Computes product and division checking for zeros on denominator")
    
    parser.add_argument('--a_factor', '-a', help="First factor in product and division", type=float)
    parser.add_argument('--b_factor', '-b', help="Second factor in product and division", type=float)

    args = parser.parse_args()
    
    run_once = MultDivClass(a=args.a_factor, b=args.b_factor)

    run_once.run()
