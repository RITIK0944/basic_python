#arr = list (map(int,input("enter your array:  ").split()))
# #arr.sort()
# def largest(arr):
#     max= arr[0]
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[j]>max:
#                 max = arr[j]
#     return max
# def secondlargest(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[j]>arr[i]:
#                 max = arr[j]
        
                
# ans = largest (arr)
# print(ans)
arr = [-1,-2,-3,-4,1,2,3,4,5,6,6,5,7,6,4,3,2,1]

# def reverse(arr):

#     n = len(arr)

#     i = 0
#     j = n - 1

#     while i < j:

#         arr[i], arr[j] = arr[j], arr[i]

#         i += 1
#         j -= 1

#     return arr

# arr = reverse(arr)

# print(arr)
# def checksorted(arr):
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             return False
#     return True
# arr=checksorted(arr)
# print(arr)
# def zeroes(arr):
#     n=len(arr)
#     j=0
#     for i in range(n):
#         if arr[i]!=0:
#             arr[i],arr[j]=arr[j],arr[i]
#             j+=1
#     return arr
# arr=zeroes(arr)
# print(arr)
# def neg(arr):
#     n=len(arr)
#     j=0
#     for i in range(n):
#         if arr[i]>0:
#             arr[i],arr[j]=arr[j],arr[i]
#             j+=1
#     return arr
# arr=neg(arr)
# print(arr)
def removeduplicate(arr):

    i = 0

    while i < len(arr):

        j = i + 1

        while j < len(arr):

            if arr[i] == arr[j]:

                arr[j] = arr[-1]
                arr.pop()

            else:
                j += 1

        i += 1

    return arr


arr = removeduplicate(arr)

print(arr)