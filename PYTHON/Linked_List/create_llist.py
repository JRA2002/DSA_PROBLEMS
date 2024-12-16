# init the class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# insert a new node
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
        
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertNode(data)
        position = 0
        current_node = self.head
        while (current_node != None) and (position + 1 != index):
            position += 1
            current_node =current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print('not index present')

    def removeFirstNode(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def updateNode(self, val, index):
        position = 0
        current_node = self.head

        if position == index:
            current_node.data = val
        else:
            while position != index and (current_node != None):
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else:
                print('Index not present')

    def removeLastNode(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node != None and (current_node.next.next != None):
            current_node = current_node.next
        current_node.next = None
    
    def remove_at_index(self, index):
        if self.head is None:
            return

        position = 0
        current_node = self.head
        if position == index:
            self.removeFirstNode()
        else:
            while current_node != None and (position + 1 < index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print('Index Not present')
    
    def remove_middle(self):
        if self.head is None:
            return
        current = self.head
        length = 0
        while current.next != None:
            length += 1
            current = current.next
        middle = (length // 2) + 1

        if length == 1:
            return None
        position = 1
        current = self.head
        while position < middle :
            position += 1
            current = current.next
        current.next = current.next.next
        
            
    def remove_node_by_value(self, data):
        current_node = self.head
        if current_node.data == data:
            self.removeFirstNode()
            return
        else:
            while current_node != None and current_node.next.data != data:
                current_node = current_node.next
            if current_node == None:
                return
            else:
                current_node.next = current_node.next.next
    def remove_duplicate(self):
        temp = self.head.data
        current = self.head
        print(current.data)
        position = 0
        while current != None:
            current.data
            position += 1
            current = current.next
    


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
                    
                    

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
        


llist = LinkedList()

llist.insertNode(5)
llist.insertNode(3)
llist.insertNode(3)
llist.insertNode(2)
llist.insertNode(1)

print("Node Data")
llist.printLL()
llist.remove_duplicate()
print("size of linked list")
llist.printLL()




        
        