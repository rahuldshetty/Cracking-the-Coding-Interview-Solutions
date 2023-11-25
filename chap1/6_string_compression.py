'''
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite

ts = TestSuite() \
    .add_test("aabcccccaaa", "a2b1c5a3") \
    .add_test("aa", "aa")   \
    .add_test("aaa", "a3")


def check1(s):
    new_s = ""
    
    prev = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            new_s += s[i-1] + str(count)
            count = 1
            prev = s[i]
    new_s += prev + str(count)
    if len(new_s) < len(s):
        return new_s
    return s

ts.run(check1)

    