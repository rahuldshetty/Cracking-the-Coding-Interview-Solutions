'''
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite

ts = TestSuite() \
    .add_test("Mr John Smith    ", "Mr%20John%20Smith") \
    .add_test("M r John Smith      ", "M%20r%20John%20Smith")


def check1(s):
    n = len(s.strip())

    s = list(s)

    index = n - 1

    while index >= 0:
        if s[index] == ' ':
            for j in range(n-1, index, -1):
                s[j+2] = s[j]
            s[index] = '%'
            s[index+1] = '2'
            s[index+2] = '0'
            n = n + 2
        index -= 1

    return "".join(s)



ts.run(check1)


ts2 = TestSuite() \
    .add_test("Mr John Smith", "Mr%20John%20Smith") \
    .add_test("M r John Smith", "M%20r%20John%20Smith") \
    .add_test("M  4", "M%20%204")

def check2(s):
    n = len(s)
    c = s.count(' ')

    s = s + "  " * c
    s = list(s)

    index = n + c * 2  - 1
    
    for i in range(n-1, -1, -1):
        if s[i] == ' ':
            s[index] = '0'
            s[index - 1] = '2'
            s[index - 2] = '%'
            index -= 3
        else:
            s[index] = s[i]
            index -= 1 

    return ''.join(s)

ts2.run(check2)