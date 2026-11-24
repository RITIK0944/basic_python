class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def removeduplicate(head):
        curr = head
        if curr == None or curr.next == None:
            return head
        while curr.next != None:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
#     head =Node(1)
#     head.next = Node(2)
#     head.next.next = Node(2)
#     head.next.next.next = Node(3)
#     head.next.next.next.next = Node(3)
#    # printLinkedList(head)
#     removeduplicate(head)
#    # printLinkedList(head) 