'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reverse_LL(self, head):
        prev = None
        
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
            
        return prev

