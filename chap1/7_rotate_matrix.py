'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place?
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite

ts = TestSuite() \
    .add_test([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]) \
    .add_test([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
    
def transpose(m):
    n = len(m)
    for i in range(n):
        for j in range(i, n):
            if i != j:
                t = m[j][i]
                m[j][i] = m[i][j]
                m[i][j] = t

def mirror(m):
    n = len(m)
    for i in range(n//2):
        for j in range(n):
            t = m[i][j]
            m[i][j] = m[ n - 1 - i][j]
            m[n - 1 - i][j] = t

def check(matrix):
    mirror(matrix)
    transpose(matrix)
    return matrix

ts.run(check)