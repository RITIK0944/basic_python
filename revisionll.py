class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
a.next=b
b.next=c
c.next=d
d.next=e
head=a
# def middleNode(head):
#     slow=head
#     fast=head
#     while fast.next!=None:
#         fast=fast.next.next
#         slow=slow.next
#     return slow
# ans = middleNode(head)
# print(ans.data)
def deletenode(head,n):
    curr= head
    while curr.next!=None:
        if curr.next.data == n :
            curr.next = curr.next.next
        else:
            curr= curr.next
    return head
ans = deletenode(head,3)
print(ans)
