'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0

https://leetcode.com/problems/set-matrix-zeroes/
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite

ts = TestSuite() \
    .add_test([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]) \
    .add_test([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]])

def check(matrix):
    m = len(matrix)
    n = len(matrix[0])

    first_col_has_zero = False
    first_row_has_zero = False

    # check if first row/col has zero or not
    for i in range(n):
        if matrix[0][i] == 0:
            first_row_has_zero = True
            break
    
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break

    # find elements where 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # nullify row
    for r in range(1, m):
        if matrix[r][0] == 0:
            for j in range( n):
                matrix[r][j] = 0
    
    # nullify col
    for c in range(1, n):
        if matrix[0][c] == 0:
            for r in range(m):
                matrix[r][c] = 0
    
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0

    if first_row_has_zero:
        for i in range(n):
            matrix[0][i] = 0

    return matrix

ts.run(check)