

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(3)
c = Node(7)

a.next = b
b.next = c
head = a

# traverse
def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    return head

printLinkedList(head)

# insertion at beginning
newNode = Node(10)
newNode.next = head
head = newNode

printLinkedList(head)

# insertion at end
newNode = Node(20)
curr = head

while curr.next is not None:
    curr = curr.next

curr.next = newNode

printLinkedList(head)
#insrtion at middle
k=2
newnode = Node(4)
curr = head 
for i in range(k-1):
    curr = curr.next
newnode.next =curr.next
curr.next = newnode
printLinkedList(head)
#deletion at start
head = head.next
printLinkedList(head)
#deletion at end
curr = head
while curr.next.next is not None:
    curr = curr.next
curr.next = None
printLinkedList(head)
#deletion in middle
k=2
curr = head
for i in range(k-1):
    curr = curr.next
curr.next = curr.next.next
printLinkedList(head)