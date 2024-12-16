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
    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def find_data_reverse(self, n):
        self.reverse()
        length = 1
        current = self.head
        while length < n:
            length += 1
            current = current.next

        data = current.data
        return data

    def rotate(self, k):
        if self.head is None:
            return self.head
        current = self.head
        lenght = 1
        while current.next != None:
            lenght += 1
            current = current.next
        if lenght == 1:
            return self.head
        
        true_k = lenght - (k % lenght)
        current.next = self.head
        
        current = self.head
        for i in range(true_k - 1):
            current = current.next
        
        self.head = current.next
        current.next = None


    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

node = LinkedList()
node.insertNode(4)
node.insertNode(3)
node.insertNode(2)
node.insertNode(1)

print("my linked list")
node.printLL()
print("find_data")
res = node.find_data(2)
print(res)

