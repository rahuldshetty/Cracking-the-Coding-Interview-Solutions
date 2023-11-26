'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting

https://leetcode.com/problems/intersection-of-two-linked-lists/
'''

class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        seen = set()

        while a != None:
            seen.add(a)
            a = a.next
        
        while b != None:
            if b in seen:
                return b
            b = b.next
        
        return None
    
######
###
###
###


def getTailSize(node):
    size = 0
    cur = node
    while cur.next != None:
        cur = cur.next
        size += 1
    return cur, size

def skipNodes(node, skip):
    cur = node
    while skip > 0 and cur != None:
        cur = cur.next
        skip -= 1
    return cur

class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        if a == None or b == None:
            return None

        # find end nodes (tail)
        tail1, n1 = getTailSize(a)
        tail2, n2 = getTailSize(b)

        # if tails dont match, then we have 2 unintersected lists
        if tail1 != tail2:
            return None

        # find the longer node
        shorter = a if n1 <= n2 else b
        longer = a if n1 > n2 else b

        # skip few nodes in the longer node
        longer = skipNodes(longer,  abs(n2 - n1))
        
        # try to find the node which is point of intersection
        while longer != shorter:
            longer = longer.next
            shorter = shorter.next
        
        return longer
