'''
Given two strings, write a method to decide if one is a permutation of the
other.
'''
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite

ts = TestSuite() \
    .add_test(("god", "dog"), True) \
    .add_test(("dof", "fog"), False) \
    .add_test(("sdof", "fog"), False) \
    .add_test(("doogere", "doogeer"), True) \
    .add_test(("dsof", "fog"), False) \
    .add_test(("dsof", ""), False) \
    

def check1(input):
    s, t = input
    n1, n2 = len(s), len(t)

    if n1 != n2:
        return False

    a = [0]*26
    for i in range(n1):
        c1 = ord(s[i]) - ord('a')
        c2 = ord(t[i]) - ord('a')
        a[c1] += 1
        a[c2] -= 1
    
    return all(x == 0 for x in a)

def check2(input):
    s, t = input
    return sorted(s) == sorted(t)

ts.run(check1)
ts.run(check2)


