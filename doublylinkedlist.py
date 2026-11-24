
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# def middleNode(head):
#     curr = head
#     l = 0

#     # count length
#     while curr is not None:
#         curr = curr.next
#         l += 1

#     # move to middle
#     curr = head
#     for i in range(l // 2):
#         curr = curr.next

#     return curr
def fastslowpointer(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

    
    


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next=f
f.next = None
head = a

ans = fastslowpointer(head)
print(ans.data)