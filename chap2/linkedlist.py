
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def append(self, data):
        # inserts a new node to end of linked list
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)
        return self

    def __str__(self):
        temp = self
        
        s = ""

        while temp.next != None:
            s = s + str(temp.data) + " -> "
            temp = temp.next

        s = s + str(temp.data) 
        
        return s

    def list(self):
        res = []
        temp = self
        while temp != None:
            res.append(temp.data)
            temp = temp.next
        return res

if __name__ == "__main__":
    nodes_to_append = list(range(2, 11))

    root = Node(1)
    print(root)
    
    for x in nodes_to_append:
        root.append(x)
    
    print(root)