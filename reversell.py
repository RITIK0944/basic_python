class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def reverse(head):
        curr = head
        prev= None
        nxt = None
        while curr!= None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        return prev