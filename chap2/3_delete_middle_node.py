'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f

Refer Similar: https://leetcode.com/problems/delete-node-in-a-linked-list/description/
'''


def delete_node(node):
    if node == None or node.next == None:
        return False
    '''
    Since head is not given, we need to copy the next node and then update the link of the current node to the next's next.
    '''
    next = node.next
    node.data = next.data
    node.next = next.next
    return True

