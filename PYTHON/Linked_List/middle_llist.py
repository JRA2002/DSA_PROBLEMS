class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def find_size(self):
        count = 0
        if self.head:
            current_node = self.head
            while current_node:
                count += 1
                current_node = current_node.next
            return count
        else:
            return -1
        
    def middle(self):
        size = self.find_size()
        index = size//2
        if size % 2 == 0:
            i = 1
        else:
            i = 0
        
        if self.head:
            current_node = self.head
           
            while current_node != None and i < index:
                i += 1
                current_node = current_node.next
            data = current_node.data
            return data



    

llist = LinkedList()
llist.insertNode(20)
llist.insertNode(15)
llist.insertNode(2)
llist.insertNode(13)
llist.insertNode(2)
llist.insertNode(10)
llist.insertNode(13)
llist.insertNode(3)
llist.insertNode(2)
llist.insertNode(6)

res = llist.find_size()
print(res)
midd = llist.middle()
print(midd)
