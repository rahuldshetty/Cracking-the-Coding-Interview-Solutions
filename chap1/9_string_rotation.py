'''
String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

https://leetcode.com/problems/rotate-string/description/
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite


ts = TestSuite() \
    .add_test(("waterbottle", "erbottlewat"), True) \
    .add_test(("abcde", "abced"), False)


def check1(input):
    s, goal = input
    if len(s) != len(goal):
        return False
    
    n = len(s)

    for i in range(n):
        a, b = s[:i], s[i:]
        if b + a == goal:
            return True
    
    return False


def check2(input):
    s, goal = input
    if len(s) != len(goal):
        return False
    return goal in s + s 


ts.run(check1)
ts.run(check2)