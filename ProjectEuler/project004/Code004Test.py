'''
Created on Feb 23, 2014

@author: Robert
'''
import unittest
from Code004 import *

class Test(unittest.TestCase):


    def test_is_palindrome(self):
        actual_result = is_palindrome(123321)
        self.assertTrue(actual_result, "Test case was a palindrome and returned False.")
        
    def test_is_palindrome_is_false(self):
        actual_result = is_palindrome(123322)
        self.assertFalse(actual_result, "Test case was not a palindrome and returned True.")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_is_palindrome']
    unittest.main()