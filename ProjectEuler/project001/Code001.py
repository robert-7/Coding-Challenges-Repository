'''
Created on Feb 21, 2014

@author: Robert
'''

class NotAListException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)
        
class ListNotIntsException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)

class Code001:
    def __init__(self, list_for_multiples, upper_bound):
        self.list_for_multiples = self._check_list_for_multiples(list_for_multiples)
        self.exclude_list_for_multiples = self.generate_exclude_list_for_multiples()
        self.upper_bound = upper_bound
        
    def generate_exclude_list_for_multiples(self):
        return [self.list_for_multiples[0]*self.list_for_multiples[1]]
#         for i in range(len(self.list_for_multiples))-1:
#             for j in len(i):
#                 self.exclude_list_for_multiples = 
        
    def _check_list_for_multiples(self, list_for_multiples):
        if type(list_for_multiples) is int:
            list_for_multiples = [list_for_multiples]
        if type(list_for_multiples) is not list:
            raise NotAListException("list_for_multiples is not a list")
        for i in range(len(list_for_multiples)):
            if type(list_for_multiples[i]) is not int:
                raise ListNotIntsException("Object at index {0} is not an int: {1}".format(i, str(list_for_multiples[i])))
        return list_for_multiples
            
    def __str__(self):
        return str(self.list_for_multiples) + " " + str(self.upper_bound)
    
    def find_sum(self):
        mults_and_maxes = self.get_mults_and_maxes(self.list_for_multiples)
        mults_and_maxes_div_mults = self.get_mults_and_maxes_div_mults(mults_and_maxes, self.list_for_multiples)
        sum_with_double_count = self.get_sum(mults_and_maxes_div_mults, self.list_for_multiples)
        
        mults_and_maxes_of_double_counts = self.get_mults_and_maxes(self.exclude_list_for_multiples)
        mults_and_maxes_of_double_counts_div_mults = self.get_mults_and_maxes_div_mults(mults_and_maxes_of_double_counts, self.exclude_list_for_multiples)
        sum_of_double_count = self.get_sum(mults_and_maxes_of_double_counts_div_mults, self.exclude_list_for_multiples)
        
        return sum_with_double_count - sum_of_double_count
        
    def get_sum(self, mults_and_maxes_div_mults_general, list_for_multiples_general):
        overall_sum = 0
        for mult in list_for_multiples_general:
            max_div_mult = mults_and_maxes_div_mults_general[mult]
            overall_sum += mult * max_div_mult * (max_div_mult + 1) / 2
        return overall_sum
        
    def get_mults_and_maxes_div_mults(self, mults_and_maxes, list_for_multiples_general):
        for mult in list_for_multiples_general:
            mults_and_maxes[mult] = mults_and_maxes[mult] / mult
        return mults_and_maxes
    
    def get_mults_and_maxes(self, list_for_multiples_general):
        mults_and_maxes = {}
        for mult in list_for_multiples_general:
            mults_and_maxes[mult] = self.find_associated_max(mult)
        return mults_and_maxes
    
    def find_associated_max(self, mult):
        remainder = self.upper_bound % mult
        if remainder == 0:
            remainder = mult
        associated_max = self.upper_bound - remainder
        return associated_max

if __name__ == "__main__":
    test_case = Code001([3,5],1000)
    print test_case.find_sum()