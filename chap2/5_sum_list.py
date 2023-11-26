'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.

https://leetcode.com/problems/add-two-numbers/

https://leetcode.com/problems/add-two-numbers-ii/description/
'''


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(0)

    prev = None
    cur = head
    carry = 0

    while l1 != None and l2 != None:
        val = l1.val + l2.val + carry
        cur.val = val % 10 
        carry = val // 10
        
        l1 = l1.next
        l2 = l2.next

        prev = cur
        
        cur.next = ListNode(0)
        cur = cur.next
    
    if l1 == None:
        l1 = l2

    while l1 != None:
        val = l1.val + carry
        cur.val = val % 10 
        carry = val // 10

        prev = cur
        cur.next = ListNode(0)
        cur = cur.next

        l1 = l1.next

    if carry != 0:
        cur.val = carry
    else:
        prev.next = None
    
    return head


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:
    if l1 == None and l2 == None and carry == 0:
        return None
    
    node = ListNode(0)
    
    value = carry
    if l1 != None:
        value += l1.val
    if l2 != None:
        value += l2.val
    
    node.val = value % 10

    if l1 != None or l2 != None:
        more = self.addTwoNumbers(
            l1.next if l1 else None, 
            l2.next if l2 else None,
            value // 10
        )
        node.next = more

    return node


