'''
Created on Feb 23, 2014

@author: Robert
'''

def get_largest_prime_factor(n):
    #handle the case where n is 1
    if n == 1:
        return 1
    
    #otherwise n is greater than one, so we can expect the largest prime
    #factor to be greater than one
    largest_prime = 2
    
    #now we can try to find the divisors of n
    current_test_prime = largest_prime
    remainder = n % current_test_prime
    while n != 1:
        while remainder != 0:
            # we didn't find a factor
            #increment current_test_prime by 1
            current_test_prime += 1
            remainder = n % current_test_prime
        largest_prime = current_test_prime
        
        #Euclid's Lemma let's us do this
        n = n / largest_prime
        remainder = n % current_test_prime
    
    return largest_prime
        

if __name__ == "__main__":
    print get_largest_prime_factor(600851475143)