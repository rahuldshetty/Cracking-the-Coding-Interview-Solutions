'''
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

Input:
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output:
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

https://leetcode.com/problems/partition-list/
'''



def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    before_x = ListNode(0)
    after_x = ListNode(0)

    before = before_x
    after = after_x

    cur = head
    while cur:
        if cur.val < x:
            before.next = cur
            before = before.next
        else:
            after.next = cur
            after = after.next
        cur = cur.next

    before.next = after_x.next
    after.next = None
    
    return before_x.next