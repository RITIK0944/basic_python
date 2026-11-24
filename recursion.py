#print name n times
# def printname(name,n):
#     if n==0:
#         return
#     print(name)
#     printname(name,n-1)

# printname("ritik",5)
#n to 1 number print
# def printnumber(n):
#     if n==0:
#         return
#     print(n)
#     printnumber(n-1)

# printnumber(5)
#1 to n number print
# def printnumber(n):
#     if n==0:
#         return
#     printnumber(n-1)
#     print(n)

# printnumber(5)
# 1 to n 
# def linearalyy(i,n):
#     if i==n+1:
#         return
#     print(i) 
#     linearalyy(i+1,n)
  
# linearalyy(1,5)
#1 to n number sum
# def sum1(i,n):
#     if i==n:
#         return i
#     return i+sum1(i+1,n)
# print(sum1(1,5))
#2nd approach
# def sum1(n):
#     if n==0:
#         return 0
#     return n+sum1(n-1)
# n= int (input('enter the number : '))
# print('sum is : ',sum1(n))
#reverse array
# arr=[1,2,3,4,2]
# def reverse(i,j):
#     if i>j:
#         return
#     arr[i],arr[j]=arr[j],arr[i]
#     reverse(i+1,j-1)
# reverse(0,len(arr)-1)
# print(arr)
#2nd approaach
# def reverse(arr,i):
#     if i>=len(arr)/2:
#         return
#     arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
#     reverse(arr,i+1)
# reverse(arr,0)
# print(arr)
#palindrome check
# s='madam'
# n=len(s)

# def ispalindrome(i):
#     if (i>=n//2):
#         return True
#     if (s[i]!=s[n-i-1]):
#         return False
#     return ispalindrome(s,i+1,n) 
# print(ispalindrome(0))
#print subsequences
# arr=[1,2,3]
# def subsequences(index,arr,temp):
#     if index ==len(arr):
#         print(temp)
#         return
#     temp.append(arr[index])
#     subsequences(index+1,arr,temp)
#     temp.pop()
#     subsequences(index+1,arr,temp)
# subsequences(0,arr,[])
#insertion sort
# def selecstionsort(arr):
#     n=len(arr)
#     for i in range(0,n):
#         mini_index=i
#         for j in range(i+1,n):
#             if arr[mini_index]>arr[j]:
#                 mini_index=j
#         arr[i],arr[mini_index]=arr[mini_index],arr[i]
#     return arr

# arr=[5,7,8,4,1,6,9,2]
# arr=selecstionsort(arr)
# print(arr)
#decending order
# def decendingorder(arr):
#     n=len(arr)
#     for i in range(0,n):
#         maxi=i
#         for j in range(i+1,n):
#             if arr[maxi]<arr[j]:
#                 maxi=j
#         arr[i],arr[maxi]=arr[maxi],arr[i]
#     return arr
# arr=[5,7,8,4,1,6,9,2]
# arr=decendingorder(arr)
# print(arr)
#BUBLE SORT
# arr=[5,7,8,4,1,9,2]
# n=len(arr)
# for i in range(n-2,-1,-1):
#     for j in range(0,i+1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
        
# print(arr)
#decending order

# Descending order
# arr = [5, 1, 7, 5, 4, 5, 3, 2, 9, 0]

# n = len(arr)

# for i in range(n):
#     for j in range(n - 1):
#         if arr[j] < arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print(arr)
#insertion sort
# n=[3,5,6,4,7,8,9,1,3,1]
# def insertion_sort(n):
#     for i in range(1,len(n)):
#         key=n[i]
#         j=i-1
#         while(j>=0 and key<n[j]):
#             n[j+1]=n[j]
#             j-=1
#         n[j+1]=key
#     return n
# print(insertion_sort(n))
#merge sortt
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid = len(arr)//2
#     left_arr=[: mid]
#     right_arr=[mid :]

#     left=merge_sort(left_arr)
#     right=merge_sort(right_arr)
# arr=[4,6,3,5,7,8,3,9]

# def merge_array(left,right):
#     result=[]
#     i,j=0,0
#     n,m=len(left),len(right)
#     while i<n and j<m:
#         if left[i]<=right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     if i<n:
#         while i < n:
#             result.append(left[i])
#             i+=1
#     if j<m:
#         while j<m:
#             result.append(right[j])
#             j+=1
#     return result
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid = len(arr)//2
#     left_arr=arr[: mid]
#     right_arr=arr[mid :]

#     left=merge_sort(left_arr)
#     right=merge_sort(right_arr)
#     return merge_array(left,right)
# print(merge_sort(arr))
#quick sort

#arr = [3, 6, 2, 1, 9, 0, 4]

# def partition(arr, low, high):
#     pivot = arr[low]
#     i, j = low, high

#     while i < j:
#         while i <= high and arr[i] <= pivot:
#             i += 1

#         while j >= low and arr[j] > pivot:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[low], arr[j] = arr[j], arr[low]
#     return j


# def quick_sort(arr, low, high):
#     if low < high:
#         partition_index = partition(arr, low, high)
#         quick_sort(arr, low, partition_index - 1)
#         quick_sort(arr, partition_index + 1, high)

#     return arr


# print(quick_sort(arr, 0, len(arr) - 1))
#binary search
# def binarysearch(arr,target):
#     n=len(arr)
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# arr=[1,2,3,4,5,6,7,8,9]
# target=18
# print(binarysearch(arr,target))
#recursive approach
# def binarysearch(arr,target,low,high):
#     if low>high:
#         return -1
#     mid=(low+high)//2
#     if arr[mid]==target:
#         return mid
#     elif arr[mid]<target:
#         return binarysearch(arr,target,mid+1,high)
#     else:
#         return binarysearch(arr,target,low,mid-1)
# arr=[1,2,3,4,5,6,7,8,9]
# target=6
# print(binarysearch(arr,target,0,len(arr)-1))
#lower bound
arr = [1,1,1,2,3,3,4,5,5,6,6,6,7]
def lowerbound(arr, target):
    n = len(arr)
    lb = n
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb
print(lowerbound(arr, 4))
