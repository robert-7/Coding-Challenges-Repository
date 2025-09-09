'''
Created on Feb 21, 2014

@author: Robert
'''
import unittest
from Code001 import *

class Test(unittest.TestCase):


    def test_1_single_lists_allowed(self):
        try:
            test_case = Code001(1,2)
        finally:
            expected_result = "[1] 2"
            actual_result = str(test_case)
            self.assertEqual(actual_result, expected_result, "Expected result: {0}. Actual result: {1}.".format(expected_result, actual_result))
    
    def test_1_nonlists_nonints_disallowed(self):
        self.assertRaises(NotAListException, Code001, "hello", 2)
        
    def test_1_list_must_contain_ints(self):
        self.assertRaises(ListNotIntsException, Code001, [1,"b"] ,2)

    def test_2_find_associated_max(self):
        try:
            test_case = Code001(3,1000)
            actual_result = test_case.find_associated_max(3)
        finally:
            expected_result = 999
            self.assertEqual(actual_result, expected_result, "Expected result: {0}. Actual result: {1}.".format(expected_result, actual_result))

    def test_2_get_mults_and_max(self):
        try:
            test_case = Code001([3,5],1000)
            actual_result = test_case.get_mults_and_maxes()
        finally:
            expected_result = {3:999,5:995}
            self.assertEqual(actual_result, expected_result, "Expected result: {0}. Actual result: {1}.".format(expected_result, actual_result))

    def test_2_get_mults_and_maxes_div_mults(self):
        try:
            test_case = Code001([3,5],1000)
            actual_result = test_case.get_mults_and_maxes_div_mults({3:999,5:995})
        finally:
            expected_result = {3:333,5:199}
            self.assertEqual(actual_result, expected_result, "Expected result: {0}. Actual result: {1}.".format(expected_result, actual_result))

    def test_2_get_sum(self):
        try:
            test_case = Code001([3,5],1000)
            actual_result = test_case.get_sum_with_double_count({3:333,5:199})
        finally:
            expected_result = {}
            self.assertEqual(actual_result, expected_result, "Expected result: {0}. Actual result: {1}.".format(expected_result, actual_result))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()