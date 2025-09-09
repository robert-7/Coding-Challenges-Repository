'''
Created on Feb 23, 2014

@author: Robert
'''
import unittest
from Code003 import *

class Test(unittest.TestCase):


    def test_print_largest_prime_factor_general(self):
        actual_result = get_largest_prime_factor(13195)
        expected_result = 29
        self.assertEqual(actual_result, 
                         expected_result, 
                         "Expected result: {0}. Actual result: {1}.".format(expected_result, actual_result))
    
    def test_print_largest_prime_of_prime_number(self):
        actual_result = get_largest_prime_factor(53)
        expected_result = 53
        self.assertEqual(actual_result, 
                         expected_result, 
                         "Expected result: {0}. Actual result: {1}.".format(expected_result, actual_result))
        
    def test_print_largest_prime_of_with_factors_of_greater_multiplicity(self):
        # n = 75 = 3*5*5
        actual_result = get_largest_prime_factor(75)
        expected_result = 5
        self.assertEqual(actual_result, 
                         expected_result, 
                         "Expected result: {0}. Actual result: {1}.".format(expected_result, actual_result))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()