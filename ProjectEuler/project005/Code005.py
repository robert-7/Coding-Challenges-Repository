'''
Created on Feb 23, 2014

@author: Robert
'''

if __name__ == "__main__":
    n = 2*3*2*5*7*2*3*11*13*17*2*19
    for i in range(1,21):
        if (n % i) != 0:
            print "{0} does not divide {1}".format(i,n)
        else:
            print "{0} divides {1}".format(i,n)