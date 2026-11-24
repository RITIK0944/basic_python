#bubble sort
# nums=[5,2,3,1]

# def sort(nums):
#     n=len(nums)
#     for i in range(n):
#         for j in range(n-i-1):
#             if nums[j]>nums[j+1]:
#                 #swap
#                 temp=nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j+1]=temp

#     return nums
# print(sort(nums))
#insertion sort
# def insertion(nums):
#     n = len (nums)
#     for i in range(1,n):
#         key=nums[i]
#         j=i-1
#         while j>=0 and nums[j]>key:
#             nums[j+1]=nums[j]

#             j-=1
#         nums[j+1]=key

#     return nums
# nums=[3,4,8,5,6,7]
# print(insertion(nums))
#selection sort
# arr=[1,3,4,5,8,7]
# def selection(arr):
#     n=len(arr)
#     for i in range(n):
#         mn=arr[i]
#         ind=i
#         for j in range(i+1,n):
#             if arr[j]<mn:
#                 mn = arr[j]
#                 ind=j
#             temp=arr[i]
#             arr[i]=arr[ind]
#             arr[ind]=temp
#     return arr
# print(selection(arr))
#merge sort
def merge(nums,l,mid,r):
    a=[]
    b=[]
    for i in range(l,mid+1):
        a.append[i]
    for i in range(mid+1,r+1):
        b.append[i]
    i,j,k=0,0,1
    while k<=r:
        if j==len(b)
def mergeSort(nums,l,r):
    if l>=r:
        return
    mid=(l+r)//2 
    mergeSort(nums,l,mid)
    mergeSort(nums,mid+1,r)



