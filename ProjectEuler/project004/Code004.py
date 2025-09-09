'''
Created on Feb 23, 2014

@author: Robert
'''

def find_largest_palindrome(n1,n2):
    largest_product = 0
    largest_n1 = 0
    largest_n2 = 0
    while n1 != 0:
        product = n1 * n2
        while not is_palindrome(product):
            #store it
            n2 -= 1
            product = n1 * n2
        if product > largest_product:
            largest_product = product
            largest_n1 = n1
            largest_n2 = n2
        n1 -= 1
        n2 = n1
    return "Product: {0}\tlargest_n1: {1}\tlargest_n2: {2}".format(largest_product, largest_n1, largest_n2)
    
def is_palindrome(n):
    str_n = str(n)
    reverse_str_n = str_n[::-1]
    return str_n == reverse_str_n

if __name__ == "__main__":
    print find_largest_palindrome(99,99)
    print find_largest_palindrome(999,999)