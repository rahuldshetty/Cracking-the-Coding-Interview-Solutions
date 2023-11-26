'''
Palindrome: Implement a function to check if a linked list is a palindrome.

https://leetcode.com/problems/palindrome-linked-list/
'''

def reverse(node):
    if not node:
        return
    head = None
    while node != None:
        n = ListNode(node.val)
        n.next = head
        head = n
        node = node.next
    return head

def is_equal(a, b):
    while a and b:
        if a.val != b.val:
            return False
        a = a.next
        b = b.next
    return a == None and b == None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        t = head

        prev_mapping = {}

        while t != None:
            prev_mapping[t] = prev
            prev = t
            t = t.next
        
        s = head
        
        while s != None and prev != None and s.val == prev.val:
            s = s.next
            prev = prev_mapping[prev]
        
        return (s != None and prev != None and s.val == prev.val) or (s == None and prev == None)


######

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head and  head.next == None:
            return True

        slow, fast = head, head
        
        stack = []

        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        
        if fast != None:
            slow = slow.next
        
        while slow != None:
            if slow.val != stack[-1]: return False
            stack.pop()
            slow = slow.next
        
        return True