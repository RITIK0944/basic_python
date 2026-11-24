# #search inserted position
# # def lower_bound(nums, target):
# #     n = len(nums)
# #     lb = n
# #     low = 0# #     high = n - 1
# #     while low <= high:
# #         mid = (low + high) // 2
# #         if nums[mid] >= target:
# #             lb = mid
# #             high = mid - 1
# #         else:
# #             low = mid + 1
# #     return lb
# # nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
# # target = 16
# # print(lower_bound(nums, target))
# #cell the floor
# def floor_ceil(nums, target):
#     n = len(nums)
#     floor = float('-inf')
#     ceil = float('inf')
#     low = 0
#     high = n - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] == target:
#             return [nums[mid], nums[mid]]
#         elif nums[mid] < target:
#             floor = nums[mid]
#             low = mid + 1
#         else:
#             ceil = nums[mid]
#             high = mid - 1
#     if floor == float('-inf'):
#         floor = -1
#     if ceil == float('inf'):
#         ceil = -1
#     return [floor, ceil]
# nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
# target = int(input("Enter the number: "))
# print(floor_ceil(nums, target))

#find first and last occurance
# nums=[2,4,6,6,6,8,12]
# target=6
# for i in range(len(nums)):
#     if nums[i]==target:
#         first=i
#         break
# for i in range(len(nums)-1,-1,-1):
#     if nums[i]==target:
#         last=i
#         break
# print([first,last])
#optimal

# def first_last(nums, target):
#     n = len(nums)
#     low, high = 0, n - 1
#     first = last = -1

#     # First occurrence
#     while low <= high:
#         mid = (low + high) // 2

#         if nums[mid] >= target:
#             if nums[mid] == target:
#                 first = mid
#             high = mid - 1
#         else:
#             low = mid + 1

#     # Last occurrence
#     low, high = 0, n - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if nums[mid] <= target:
#             if nums[mid] == target:
#                 last = mid
#             low = mid + 1
#         else:
#             high = mid - 1

#     return [first, last]


# # nums = [1, 2, 4, 4, 4, 4, 6, 7]
# target = 6

# print(first_last(nums, target))
#count occurnce of number
# nums=[1,2,4,4,4,4,6,7]
# target=4
# def count(nums,target):
#     n=len(nums)
#     count=0
#     for i in range(n):
#         if nums[i]==target:
#             count+=1
#     return count

# print(count(nums,target))
#search in rotated array
# nums=[12,12,12,13,13,13,14,1,1,2,3,4,5]
# target=12
# def binary(nums,target):
#     n=len(nums)
#     low,high=0,n-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]==target:
#             return 0
#         if nums[mid]>target:
#             high=mid-1
#         else:
#             low=mid+1

#find minimum in rotated sorted array
# nums = [4,5,6,7,0,1,2]
# minimum = nums[0]
# n = len(nums)
# i, j = 0, n-1
# while i <= j:
#     if nums[i] <= nums[j]:
#         minimum = min(minimum, nums[i])
#         break
#     mid = (i+j)//2
#     minimum = min(minimum, nums[mid])
#     if nums[mid] >= nums[i]:
#         i = mid+1
#     else:
#         j = mid-1
# print(minimum)
#2nd approach
# for i in range (1,n-1):
#     if nums[i]<minimum:
#         minimum=nums[i]
# print(minimum)
#3rd approach

# nums = [4,5,6,7,0,1,2]

# def find_min(nums):
#     low, high = 0, len(nums)-1

#     while low < high:
#         mid = (low+high)//2

#         if nums[mid] > nums[high]:
#             low = mid+1
#         else:
#             high = mid

#     return nums[low]

# print(find_min(nums))
#how many time array been rotated
arr=[3,4,5,1,2]
# for i in range(len(arr)):
#     if arr[i]<arr[i-1]:
#         print(i)
# #2nd 
# n=len(arr)
# low,high=0,n-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]>arr[mid+1]:
#         print(mid+1)
#         break
#     elif arr[mid-1]>arr[mid]:
#         print(mid)
#         break
#     elif arr[low]<=arr[mid]:
#         low=mid+1
#     else:
#         high=mid-1
#single element in arr
# arr = [1,1,2,2,3,3,4,5,5,6,6]
# result = 0
# for num in arr:
#     result ^= num
# print(result)

# arr = [1,1,2,2,3,3,4,4,5,6,6,7,7]

# def f(arr, n):
#     low, high = 0, n-1

#     while low < high:
#         mid = (low+high)//2

#         if mid % 2 == 1:
#             mid -= 1

#         if arr[mid] == arr[mid+1]:
#             low = mid+2
#         else:
#             high = mid

#     return arr[low]

# print(f(arr, len(arr)))
#find peak in mountain array
# arr=[1,3,4,5,6,4,3,2,1]
# def f(arr,n):
#     low,high=0,n-1
#     while low<high:
#         mid=(low+high)//2
#         if arr[mid]>arr[mid+1]:
#             high=mid
#         else:
#             low=mid+1
#     return arr[low]
# print(f(arr,len(arr)))
#pivot element
# arr=[50,60,70,10,20,30,40]
# def f(arr,n):
#     low,high=0,n-1
#     while low<high:
#         mid=(low+high)//2
#         if arr[mid]>arr[n-1] and arr[mid+1]>arr[mid]:
#             return mid
#         elif arr[mid]>arr[mid-1]:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# print(f(arr,len(arr)))
#sqrt of number

# def sqrt(n):
#     low=1
#     high=n
#     ans=0
#     while low<=high:
#         mid=(low+high)//2
#         if mid*mid==n:
#             return mid
#         elif mid*mid<n:
#             ans=mid
#             low=mid+1
#         else:
#             high=mid-1
#     return ans
# print(sqrt(10002223455433))
#nt root of m
# def root (n,m):
#     low=1
#     high=n
#     ans=0
#     while low<=high:
#         mid=(low+high)//2
#         if mid**m==n:
#             return mid
#         elif mid**m<n:
#             ans=mid
#             low=mid+1
#         else:
#             high=mid-1
#     return ans
# print(root(27,5))
#koko eat banana
# plus=[3, 6 ,7,11]
# h=8
# low,high=0,max(plus)

# def b(arr,h):
#     h=8
#     low,high=0,max(plus)
#     while low <=high:
#         mid= (low+high)//2
#         hours =0
#         for i in plus:
#             hours+=(plus)
#minimum no of days to malen M bouquets
# def is_possible(arr, m, max_pages):
#     students = 1
#     pages = 0
#     for book in arr:
#         if pages + book <= max_pages:
#             pages += book
#         else:
#             students += 1
#             pages = book
#     return students <= m
# def book_allocation(arr, m):
#     if m > len(arr):
#         return -1
#     low = max(arr)
#     high = sum(arr)
#     ans = high
#     while low <= high:
#         mid = (low + high) // 2
#         if is_possible(arr, m, mid):
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
# arr = [10, 20, 30, 40]
# m = 2
# print(book_allocation(arr, m))
#painter partion problem
# def is_possible(arr, k, max_time):
#     painters = 1
#     board_time = 0
#     for board in arr:
#         if board_time + board <= max_time:
#             board_time += board
#         else:
#             painters += 1
#             board_time = board

#     return painters <= k
# def painter_partition(arr, k):
#     if k > len(arr):
#         return -1
#     low = max(arr)
#     high = sum(arr)
#     ans = high
#     while low <= high:
#         mid = (low + high) // 2
#         if is_possible(arr, k, mid):
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
# arr = [10, 20, 30, 40]
# k = 2
# print(painter_partition(arr, k)
#eko spoj problem

# def is_possible(tree, m, max_height):
#     flowers = 0
#     for i in range(len(tree)):
#         if tree[i] > max_height:
#             flowers += tree[i] - max_height
#     return flowers >= m
# def tree(tree, m):
#     n = len(tree)
#     maxi = 0
#     for i in range(n):
#         if tree[i] > maxi:
#             maxi = tree[i]
#     low = 0
#     high = maxi
#     ans = 0
#     while low <= high:
#         mid = (low + high) // 2

#         if is_possible(tree, m, mid):
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1

#     return ans
# arr = [20, 15, 10, 17]
# m = 7
# print(tree(arr, m))
