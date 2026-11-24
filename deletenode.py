
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def deletenode(self, head, n):
        p1 = head
        p2 = head

        for i in range(n):
            p1 = p1.next

        if p1 == None:
            head = head.next
            return head

        while p1.next != None:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next
        return head


Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6=Node(6)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next=Node6



head = Node1
head = Node1.deletenode(head, 4)

curr = head
while curr != None:
    print(curr.data, end=" ")
    curr = curr.next