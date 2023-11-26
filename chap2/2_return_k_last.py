'''
Return Kth to Last:
Implement an algorithm to find the kth to last element of a singly linked list.

Assuming 1-idexed

Possible Solutions:
1. if length is known, then get (length - k) and traverse that many times.
2. traverse and store data in list, then return kth element from end.
3. recursive


Similar Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite
from linkedlist import Node


ts = TestSuite() \
    .add_test((Node(1).append(1).append(2).append(3).append(4), 2), 3)  \
    .add_test((Node(1).append(1).append(2).append(3).append(4), 5), 1)  \
    .add_test((Node(1).append(1).append(2).append(3).append(4), 1), 4)  \
    .add_test((Node(1).append(1).append(2).append(3).append(4), 8), -1)

def check1(input):
    '''
    Time: O(N)
    Space: O(N)
    '''
    node, k = input
    cur = node
    res = []
    while cur != None:
        res.append(cur.data)
        cur = cur.next
    if k > len(res) or k <= 0:
        return -1
    return res[-k]

def check2(input):
    '''
    Time: O(N)
    Space: O(N)
    '''
    node, k = input
    val = None

    def get_kth_node(head):
        nonlocal val, k
        if head == None:
            return 0
        index = get_kth_node(head.next) + 1
        if index == k:
            val =  head.data
        return index

    get_kth_node(node)
    
    return val if val != None else -1

def check3(input):
    '''
    Time: O(N)
    Space: O(1)
    '''
    node, k = input

    p1 = node
    p2 = node

    # move p1 k nodes above
    for _ in range(k):
        if p1 == None:
            return -1
        p1 = p1.next

    while p1 != None:
        p1 = p1.next
        p2 = p2.next

    return p2.data


ts.run(check1)
ts.run(check2)
ts.run(check3)