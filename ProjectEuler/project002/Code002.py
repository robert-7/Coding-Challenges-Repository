'''
Created on Feb 21, 2014

@author: Robert
'''

import math

# class Code2:
#     def __init__(self, upper_bound):
#         self.upper_bound = upper_bound
        
def generate_first_n_Fib(N):
    phi = (1+math.sqrt(5))/2
    psi = (1-math.sqrt(5))/2
    n=3
    fib = int(round((phi**(n)-psi**(n))/(phi-psi)))
    fibs_sum = 0
    while fib < N:
        fibs_sum += fib
        n+=3
        fib = int(round((phi**(n)-psi**(n))/(phi-psi)))
    print fibs_sum

if __name__ == "__main__":
#     test_case = Code2(4000000)
    generate_first_n_Fib(4000000)