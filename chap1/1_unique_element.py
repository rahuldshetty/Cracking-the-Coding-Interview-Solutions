'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite

ts = TestSuite() \
    .add_test([1, 2, 3, 4, 5], False) \
    .add_test([1, 2, 3, 4, 5, 6, 6], True) \
    .add_test([1], False) \
    .add_test([1, 4, -5, 3, -5, 5, 4, 4, 4], True) \
    .add_test([], False)

def check1(input):
    '''
    Time: O(len(input)) = O(N)
    Space: O(N)
    '''
    arr_set = set()
    for x in input:
        if x in arr_set:
            return True
        arr_set.add(x)
    return False



def check2(nums):
    '''
    Time: O(len(input)) = O(N)
    Space: O(1)
    '''
    bit = 0
    
    if len(nums) == 0: return False

    min_val = min(nums)

    for n in nums:
        if bit >> (n - min_val) & 1 == 1:
            return True
        # scale & set bit
        bit = bit | (1 << (n - min_val))
    return False
    

ts.run(check1)

ts.run(check2)