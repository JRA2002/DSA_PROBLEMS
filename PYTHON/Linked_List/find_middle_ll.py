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
    
    
    def size_llist(self):
            size = 0
            if self.head:
                current_node = self.head
                while current_node:
                    size += 1
                    current_node = current_node.next
                return size
            else:
                return 0
    def find_middle(self):
        index = (self.size_llist()) // 2
        current_node = self.head
        position = 0

        while current_node != None and (position + 1) < index:
                
                current_node = current_node.next
                position += 1
        middle = current_node.next.data
        
        return middle
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next



llist = LinkedList()
llist.insertNode(1)
llist.insertNode(2)
llist.insertNode(3)
llist.insertNode(4)
llist.insertNode(5)
llist.insertNode(6)



print("size linked list")
res = llist.size_llist()
print(res)
print("middle od the linked list")
middle = llist.find_middle()
print(middle)


         