# def findGcd(a,b):
#     if b==0:
#         return a
#     return findGcd(b,a%b)
# a=int(input("enter first number: "))
# b = int(input("enter second number: "))
# print("GCD of a and b is ",findGcd(a,b))
# def findfib(m):

#     if m==0 or m==1:
#         return m
#     return findfib(m-1)+findfib(m-2)
# answer =int(input("enter the number:"))
# ans=[]
# for i in range(0,answer+1):
#     ans.append(findfib(i))
# print(ans)
# def runningsum(nums):
#     n=len(nums)
#     ans=[0]*n
#     ans[0]=nums[0]
#     for i in range(1,n):
#         nums[i]+=nums[i-1]
#         ans[i]=nums[i]
#     return ans
# nums=[3,4,5,45,6,7,8,9,10]
# print(runningsum(nums))
# def parity(nums):
#     n=len(nums)
#     start=0
#     for i in range(1,n):
#         if nums [i]!=nums[start]:
#             start+=1
#             nums[start]=nums[i]
#     return start
# nums=[1,1,2,2,2,3,3,3,4,4,5,6,7,7,8,9,12,32]
# print(parity(nums))
# def maximumsums(nums):
#     n = len(nums)
#     max_sum = nums[0]
#     curr_sum=0
#     for i in range(n):
#         curr_sum+=nums[i]
#         if curr_sum>max_sum:
#             max_sum=curr_sum
#         if curr_sum<0:
#             curr_sum=0
#     return max_sum
# nums=[-2,3,-4,6,2,-1,4,-5,2]
# output=maximumsums(nums)
# for i in range(len(nums)):
#     print(nums[i],end=" ")
# print('\nMaximum sum of subarray is : ',output)