
# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None

# class singlylinkedlist:
#     def __init__(self):
#         self.head=None

#     def append(self,value):
#         new_node=Node(value)
#         if self.head is None:
#             self.head=new_node
#         else:
#             curr=self.head
#             while curr.next is not None:
#                 curr=curr.next
#             curr.next=new_node

#     def traversal(self):
#         if self.head is None:
#             print("empty list")
#         else:
#             curr=self.head
#             while curr is not None:
#                 print(curr.data,end=" ")
#                 curr=curr.next
#             print()

#     def insert(self,value,position):
#         new_node=Node(value)
#         if position==0:
#             new_node.next=self.head
#             self.head=new_node
#         else:
#             curr=self.head
#             prev=None
#             count=0
#             while curr is not None and count<position:
#                 prev=curr
#                 curr=curr.next
#                 count+=1
#             if prev is None:
#                 print("Invalid position")
#                 return
#             prev.next=new_node
#             new_node.next=curr

#     def delete(self,value):
#         temp=self.head
#         if temp is None:
#             print("node not found")
#             return
#         if temp.data==value:
#             self.head=temp.next
#             return
#         found=False
#         prev=None
#         while temp is not None:
#             if temp.data==value:
#                 found=True
#                 break
#             prev=temp
#             temp=temp.next
#         if found:
#             prev.next=temp.next
#         else:
#             print("node not found")

#     def mid(self):
#         fast=self.head
#         slow=self.head
#         while fast is not None and fast.next is not None:
#             slow=slow.next
#             fast=fast.next.next
#         return slow

#     def reverse(self):
#         temp=self.head
#         prev=None
#         while temp is not None:
#             front=temp.next
#             temp.next=prev
#             prev=temp
#             temp=front
#         self.head=prev
#         return self.head

# sll=singlylinkedlist()
# sll.append(10)
# sll.append(20)
# sll.append(400)
# sll.append(40)
# print("Original:")
# sll.traversal()
# sll.insert(30,2)
# print("After insert:")
# sll.traversal()
# sll.delete(10)
# print("After delete:")
# sll.traversal()
# r=sll.reverse()
# print("After reverse:")
# sll.traversal()
# middle=sll.mid()
# print("Middle:",middle.data if middle else None)
# print("Reverse head:",r.data if r else None)
