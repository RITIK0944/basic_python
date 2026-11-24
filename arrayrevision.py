#largest element
# a=[1,5,32,1,44,9,78] 
# largest=a[0]
# for i in range(1,len(a)):
#     if a[i]>largest:
#         largest=a[i]
# print(largest)
#second largest
# a=[1,5,32,1,44,9,78] 
# largest=a[0]
# for i in range(1,len(a)):
#     if a[i]>largest:
#         largest=a[i]
# second_largest=-1
# for i in range(1,len(a)):
#     if a[i]>second_largest and a[i]!=largest:
#         second_largest=a[i]
# print(second_largest)
#left rotate by 1 palace
# arr=[1,2,3,4,5]
# temp=arr[0]
# n= len(arr)
# for i in range (1,n):
#     arr[i-1]=arr[i]
# arr[n-1]=temp
# print(arr)
#left rotate array upto d place
#arr = [ 1,2,3,4,5,6,7,8,9,0]
#1st solution 
# d = int(input("enter the number of places to rotate: "))
# d=d%len(arr)
# temp=[]
# for i in range (d):
#     temp.append(arr[i])
# i=d
# while(i<len(arr)):
#     arr[i-d]=arr[i]
#     i+=1
# for i in range(len(arr)-d,len(arr)):
#     arr[i]=temp[i-(len(arr)-d)]
#print(arr)
 #2nd solution        
# for i in range (d):
#     temp=arr[0]
#     for j in range(len(arr)-1):
#         arr[j]=arr[j+1]
#     arr[len(arr)-1]=temp
#print(arr)
#3rd solution
#arr = [1,2,3,4,5,6,7,8,9,0]

# def leftrotate(arr, n, d):
#     d = d % n

#     arr[:d] = arr[:d][::-1]
#     arr[d:n] = arr[d:n][::-1]
#     arr[:n] = arr[:n][::-1]

# leftrotate(arr, len(arr), 2)

# print(arr)
#end at 0
# arr = [1,2,2,3,4,0,7,9,0,0,0,78,89,9]

# n = len(arr)
# temp = []

# for i in range(0, n):
#     if arr[i] != 0:
#         temp.append(arr[i])

# for i in range(len(temp), n):
#     temp.append(0)

# print(temp)
# arr = [1,2,2,3,4,0,7,9,0,0,0,78,89,9]

# n = len(arr)

# i = 0
# j = 0

# while i < n:

#     if arr[i] != 0:
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1
#         j += 1

#     else:
#         i += 1

# print(arr)
#find union and intersection of two sorted array
# arr1 = [1,2,2,3,4,4,4,6,6]
# arr2 = [1,2,3,3,4,4,5,6,8,8]
# set1=set(arr1)
# set2=set(arr2)
# print(set1.intersection(set2))
# print(set1.union(set2))
# #missing number
# arr = [1,2,3,5,6,7]

# n = len(arr) + 1

# sum = n * (n + 1) // 2

# s2 = 0

# for i in range(len(arr)):
#     s2 += arr[i]

# print(sum - s2) 
#2nd solution
# arr = [1,2,3,5,6,7]

# xor1 = 0
# n = len(arr)

# xor2 = 0

# for i in range(1, n+1):
#     xor2 = xor2 ^ i
#     xor1 = xor1 ^ arr[i-1]

# print("xor1 =", xor1)
# print("xor2 =", xor2)
# print("answer =", xor1 ^ xor2)
#maximum consucative ones
# arr=[1,1,0,1,1,1,0,1,1]
# count=0
# max_count=0
# for i in range(len(arr)):
#     if arr[i]==1:
#         count+=1
#     else:
#         max_count=max(max_count,count)
#         count=0
# print(max_count)   
#arr = [1,1,2,3,3,4,4,45,45]

# freq = {}

# for i in range(len(arr)):
#     if arr[i] in freq:
#         freq[arr[i]] += 1
#     else:
#         freq[arr[i]] = 1

# for i in freq:
#     if freq[i] == 1:
#         print(i)
# xor = 0
# for i in range(len(arr)):
#     xor=xor^arr[i]
# print(xor)
#longest subarray with sum k
#arr = [1,2,3,1,1,1,1,4,2,3]
# k=3
# i=0
# j=0
# sum=0
# max=arr[0]
# while(j<len(arr)):
#     sum+=arr[j]
#     while(sum>k):
#         sum-=arr[i]
#         i+=1
#     max=max(max,j-i+1)
# print(max)
#2nd approach
# k= int(input("enter the sum:"))
# left=0
# right=0
# sum=0
# max=arr[0]
# while(right<len(arr)):
#     sum+=arr[right]
#     while(sum>k):
#         sum-=arr[left]
#         left+=1
#     max=max(max,right-left+1)
# print(max)
#2 sum 
# arr=[1,2,3,4,5,6,7,8,9]
# n=len(arr)
# target=9
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]+arr[j]==target:
#             print(arr[i],arr[j])
# arr = [2, 7, 11, 15]
# target = 9

# temp = set()

# for i in range(len(arr)):

#     if target - arr[i] in temp:
#         print(target - arr[i], arr[i])

#     temp.add(arr[i])
#sort an array of 0's , 1's and 2's
# arr = [0,1,2,2,1,0,1,0,0,2,1,2,1]
# low=0
# mid=0
# high=len(arr)-1
# while(mid<=high):
#     if arr[mid]==0:
#         arr[mid],arr[low]=arr[low],arr[mid]
#         low+=1
#         mid+=1
#     elif arr[mid]==1:
#         mid+=1
#     else:
#         arr[mid],arr[high]=arr[high],arr[mid]
#         high-=1
# print(arr)
#majority element
# arr=[2,2,1,1,1,2,2]
# count=0
# for i in range(len(arr)):
#     if arr[i]==arr[i+1]:
#         count+=1
# i=0 
# j=len(arr)-1
# while(i<j):
#     if arr[i]==arr[j]:
#         print(arr[i])
#         i+=1
#         j-=1
# arr = [2, 2, 1, 1, 1, 2, 2, 1,2,2,2,2,2,2,2]

# candidate = 0
# count = 0

# for i in range(len(arr)):

#     if count == 0:
#         candidate = arr[i]
#         count = 1

#     elif arr[i] == candidate:
#         count += 1

#     else:
#         count -= 1

# count1 =0
# for i in range(len(arr)):
#     if arr[i]==candidate:
#         count1+=1
# if count1 > len(arr)//2:
#     print(candidate)
# else:
#     print("no majority element")

#max sub array
#arr=[-2,-3,4,-1,-2,1,5,-3]
#ans=7
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         sum=0
#         for k in range(i,j+1):
#             sum+=arr[k]
#         ans=max(ans,sum)
# print(ans)
#2nd approach
#kadane algorithm
# maxi=arr[0]
# currsum=0
# for i in range(len(arr)):
#     currsum+=arr[i]
#     maxi=max(maxi,currsum)
#     if currsum<0:
#         currsum=0
# print(maxi)
#rearrange the element by sign
# arr = [3, 1, -2, -5, -5, 2, -4]

# ans = [0] * len(arr)

# posIndex = 0
# negIndex = 1

# for i in range(len(arr)):

#     if arr[i] < 0:
#         if negIndex < len(arr):
#             ans[negIndex] = arr[i]
#             negIndex += 2
#         else:
#             ans[posIndex] = arr[i]
#             posIndex += 2
#     else:
#         if posIndex < len(arr):
#             ans[posIndex] = arr[i]
#             posIndex += 2

# print(ans)
#best time to buy and sell stock
# prices = [7,1,5,3,6,4]
# min=prices[0]
# profit=0
# for i in range(1,len(prices)):
#     if prices[i]<min:
#         min=prices[i]
#     profit=max(profit,prices[i]-min)
# print(profit)
#next permutation 
# arr = [3,1,2]
#leader
# arr = [10, 22, 12, 3, 0, 6]

# leader = []

# max_right = arr[-1]
# leader.append(max_right)

# for i in range(len(arr)-2, -1, -1):

#     if arr[i] > max_right:
#         leader.append(arr[i])

#     max_right = max(max_right, arr[i])

# leader.reverse()

# print(leader)
#longest consucative sequence
#arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]

# arr.sort()

# cntcurr = 1
# last_smaller = float('-inf')

# longest = 1

# for i in range(len(arr)):

#     if arr[i] - 1 == last_smaller:
#         cntcurr += 1
#         last_smaller = arr[i]

#     elif arr[i] == last_smaller:
#         continue

#     else:
#         cntcurr = 1
#         last_smaller = arr[i]

#     longest = max(longest, cntcurr)

# print(longest)
#optmal
# arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]

# s = set(arr)

# longest = 0

# for num in s:

#     # num sequence ka starting element hai
#     if num - 1 not in s:

#         cnt = 1
#         x = num

#         while x + 1 in s:
#             x += 1
#             cnt += 1

#         longest = max(longest, cnt)

# print(longest)
#set matrix zeroes

# def marksinfinity(matrix,row,coloumn):
#     n=len(matrix)
#     m=len(matrix[0])
#     for i in range(0,n):
#         if matrix[i][coloumn]!=0:
#             matrix[i][coloumn]=float('inf')
#     for j in range(0,m):
#         if matrix[row][j]!=0:
#             matrix[row][j]=float('inf')
# def setzeromatrix(self,matrix):
#     r=len(matrix)
#     c=len(matrix[0])
#     for i in range(0,r):
#         for j in range(0,c):
#             if matrix[i][j]==0:
#                 self.marks_in_inf(matrix,i,j)
    
#     for i in range(0,r):
#         for j in range(0,c):
#             if matrix[i][j]==float('inf'):
#                 matrix[i][j]=0
#     return 

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
#2nd approach
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 0, 9, 10],
#     [11, 0, 13, 14, 0],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]

# r = len(matrix)
# c = len(matrix[0])

# rowtrack = [0 for i in range(r)]
# coltrack = [0 for i in range(c)]

# # Step 1: Track rows and columns containing zero
# for i in range(r):
#     for j in range(c):
#         if matrix[i][j] == 0:
#             rowtrack[i] = -1
#             coltrack[j] = -1

# # Step 2: Make corresponding rows and columns zero
# for i in range(r):
#     for j in range(c):
#         if rowtrack[i] == -1 or coltrack[j] == -1:
#             matrix[i][j] = 0

# # Step 3: Print matrix
# for i in range(r):
#     print(matrix[i])
#3rd approach
# 
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 0, 9, 10],
#     [11, 0, 13, 14, 0],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]

# r = len(matrix)
# c = len(matrix[0])

# firstrow = False
# firstcol = False

# # Step 1: Check first row
# for j in range(c):
#     if matrix[0][j] == 0:
#         firstrow = True

# # Step 2: Check first column
# for i in range(r):
#     if matrix[i][0] == 0:
#         firstcol = True

# # Step 3: Mark rows and columns
# for i in range(1, r):
#     for j in range(1, c):
#         if matrix[i][j] == 0:
#             matrix[i][0] = 0
#             matrix[0][j] = 0

# # Step 4: Make cells zero using markers
# for i in range(1, r):
#     for j in range(1, c):
#         if matrix[i][0] == 0 or matrix[0][j] == 0:
#             matrix[i][j] = 0

# # Step 5: Zero the first row
# if firstrow:
#     for j in range(c):
#         matrix[0][j] = 0

# # Step 6: Zero the first column
# if firstcol:
#     for i in range(r):
#         matrix[i][0] = 0

# # Print matrix
# for row in matrix:
#     print(row) 
#90 degree rotate
# optimal solution
# matrix=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
#     ]
# n=len(matrix)
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
# for i in range(0,n):
#     matrix[i].reverse()
# print(matrix)
#1st approach

# n=len(matrix)
# result=[[0 for i in range(n)] for j in range(n)]
# for i in range(n):
#     for j in range(n):
#         result[j][n-1-i]=matrix[i][j]
# print(result)
#spiral matrix
# matrix=[
#     [20,21,22,23,24],
#     [19,32,33,34,25],
#     [18,31,36,35,26],
#     [17,30,29,28,27],
#     [16,15,14,13,12]
# ]
# result=[]
# top,left=0,0
# bottom,right=len(matrix)-1,len(matrix[0])-1
# while(top<=bottom and left<=right):
#     for k in range(left,right+1):
#         result.append(matrix[top][k])
#     top+=1
#     for k in range(top,bottom+1):
#         result.append(matrix[k][right])
#     right-=1
#     for k in range(right,left-1,-1):
#         result.append(matrix[bottom][k])
#     bottom-=1
#     for k in range(bottom,top-1,-1):
#         result.append(matrix[k][left])
#     left+=1
# print(result)
# 3 sum
#arr=[-1,0,1,2,-1,-4]

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         for k in range(j+1,len(arr)):
#             if arr[i]+arr[j]+arr[k]==0:
#                 print(arr[i],arr[j],arr[k])
#better approach
# ans=set()
# for i in range(len(arr)):
#     hashmap=set()
#     for j in range(i+1,len(arr)):
#         third=-(arr[i]+arr[j])
#         if third in hashmap:
#             ans.add((arr[i],arr[j],third))
#         hashmap.add(arr[j])
# print(ans)
#optimal approach 

# arr = [-1, 0, 1, 2, -1, -4]

# arr.sort()
# n = len(arr)
# ans = []

# for i in range(n - 2):

#     if i > 0 and arr[i] == arr[i - 1]:
#         continue

#     left = i + 1
#     right = n - 1

#     while left < right:
#         total = arr[i] + arr[left] + arr[right]

#         if total == 0:
#             ans.append([arr[i], arr[left], arr[right]])
#             left += 1
#             right -= 1

#             while left < right and arr[left] == arr[left - 1]:
#                 left += 1

#             while left < right and arr[right] == arr[right + 1]:
#                 right -= 1

#         elif total < 0:
#             left += 1

#         else:
#             right -= 1

# print(ans)
#4 sum

#arr = [1, 0, -1, 0, -2, 2]
# target = 0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         for k in range(j+1,len(arr)):
#             for l in range(k+1,len(arr)):
#                 if arr[i]+arr[j]+arr[k]+arr[l]==target:
#                     temp=[arr[i],arr[j],arr[k],arr[l]]
#                     temp.sort()
#                     print (temp)

#better approach
# ans=set()
# for i in range(len(arr)):
#     hashmap=set()
#     for j in range(i+1,len(arr)):
#         for k in range(j+1,len(arr)):
#             fourth=-(arr[i]+arr[j]+arr[k])
#             if fourth in hashmap:
#                 ans.add((arr[i],arr[j],arr[k],fourth))
#             hashmap.add(arr[j])
# print(ans)  
#missing and reapiting

# arr = (4, 3, 6, 2, 1, 1)

# repeating = []
# missing = []

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j] and arr[i] not in repeating:
#             repeating.append(arr[i])

# for i in range(1, len(arr) + 1):
#     if i not in arr:
#         missing.append(i)

# print("Missing:", missing)
# print("Repeating:", repeating)
#optimal solution

# arr = [4, 3, 6, 2, 1, 1]

# seen = set()
# repeating = []
# missing = []

# for num in arr:
#     if num in seen:
#         repeating.append(num)
#     seen.add(num)

# for i in range(1, len(arr) + 1):
#     if i not in seen:
#         missing.append(i)

# print("Repeating:", repeating)
# print("Missing:", missing)
# nums=[17,18,20,1,3,4,5,7,8,10]
# target=1
# def binary(nums,target):
#     n=len(nums)
#     low,high=0,n-1
#     while(low<=high):
#         mid=(low+high)//2
#         if nums[mid]==target:
#             return mid
#         if nums[mid]<=nums[high]:
#             if nums[mid]<=target<=nums[high]:
#                 low=mid+1
#             else:
#                 high=mid-1
#         else:
#             if nums[low]<=target<=nums[mid]:
#                 high=mid-1
#             else:
#                 low=mid+1
#     return -1
# print(binary(nums,target))
