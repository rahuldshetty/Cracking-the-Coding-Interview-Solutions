'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite

ts = TestSuite() \
    .add_test("Tact Coa", True) \
    .add_test("aabcd", False) \
    .add_test("", True)

def check(s):
    s = s.lower()

    arr = [0] * 26
    idx = lambda x:ord(x) - ord('a')

    for c in s:
        if c.isalpha():
            arr[idx(c)] += 1

    seen_odd_count = False
    for i in range(26):
        if arr[i] % 2 == 1:
            if seen_odd_count:
                return False
            else:
                seen_odd_count = True
    return True        

def check2(s):
    s = s.lower()
    bit = 0
    idx = lambda x:ord(x) - ord('a')

    for c in s:
        if c.isalpha():
            i = idx(c)
            mask = (1 << i)
            if bit & mask > 0:
                bit = bit & ~mask
            else:
                bit = bit | mask
    
    return bit == 0 or ((bit - 1) & bit == 0) 
    

ts.run(check)
ts.run(check2)