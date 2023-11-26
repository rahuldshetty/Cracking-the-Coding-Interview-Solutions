'''
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input:
A -> B -> C -> D -> E -> C [the same C as earlier]

Output:
C
'''

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break
        
        if fast == None or fast.next == None:
            return None
        
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast