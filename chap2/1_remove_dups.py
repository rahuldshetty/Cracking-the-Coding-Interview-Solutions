'''
R�mov� Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import TestSuite
from linkedlist import Node


ts = TestSuite() \
    .add_test(Node(1).append(1).append(2).append(3).append(4), [1, 2, 3, 4])  \
    .add_test(Node(1).append(1).append(2).append(4).append(4), [1, 2, 4])  \
    .add_test(Node(0).append(1).append(1).append(4), [0, 1, 4])  \
    .add_test(Node(0).append(0), [0])  \
    .add_test(Node(0), [0])  \
    .add_test(None, [])  \

def remove_duplicates1(head):
    '''
    Time Complexity: O(N)
    Space Complexity: O(N) can be reduce to O(1) with bit vector
    '''
    if not head:
        return []
    
    seen = set()
    
    prev = head
    cur = head.next

    seen.add(head.data)

    while cur != None:
        if cur.data in seen:
            prev.next = cur.next
        
        seen.add(cur.data)

        prev = cur
        cur = cur.next
    
    return head.list()


def remove_dups2(head):
    '''
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    '''
    if not head:
        return []
    
    cur = head
    while cur != None:
        runner = cur
        while runner.next != None:
            if runner.next.data == cur.data:
                runner.next = runner.next.next
            runner = runner.next
        cur = cur.next

    return head.list()

ts.run(remove_duplicates1)
ts.run(remove_dups2)

