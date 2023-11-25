'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale,  bale -> true
pale,  bake -> false
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite

ts = TestSuite() \
    .add_test(("pale", "ple"), True) \
    .add_test(("pales", "pale"), True) \
    .add_test(("pale", "bale"), True) \
    .add_test(("pale", "bake"), False) \
    .add_test(("pale", "pale"), True)

def one_edit_replace(s1, s2):
    found_diff = False
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if found_diff:
                return False
            found_diff = True
    return True

def one_edit_insert(s1, s2):
    # s1 > s2
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            i += 1
        else:
            i += 1
            j += 1
    return True
 
def check1(input):
    s1, s2 = input
    n1, n2 = len(s1), len(s2)

    if n1 == n2:
        return one_edit_replace(s1, s2)
    elif n1 > n2:
        return one_edit_insert(s1, s2)
    elif n1 < n2:
        return one_edit_insert(s2, s1)

    return False

ts.run(check1)


def check2(input):
    s1, s2 = input
    n1, n2 = len(s1), len(s2)

    if abs(n1 - n2) > 1:
        return False

    shorter_str = s1 if n1 < n2 else s2 
    longer_str = s2 if n1 < n2 else s1
    
    i, j = 0, 0

    found_diff = False

    while i < n1 and j < n2:
        if shorter_str[i] != longer_str[j]:
            if(found_diff):
                return False
            found_diff = True

            if n1 == n2:
                i += 1
        else:
            i += 1
        j += 1

    return True

ts.run(check2)