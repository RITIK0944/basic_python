# set1={2,1,"hello",2,4,1,"hello"}
# # print(set1)
# # print(len(set1))
# # list1=[1,2,2,3,4,5,6,7,87,8,7,9,6.8,1]
# # set2=set(list1)
# # print(set2)
# set1.add('100')
# print(set1)
# set1.discard("hello")
# # set1.remove("100")
# set1={1,2,3,4,5}
# set2={2,3,4,5,6,7}
# #union
# print(set1|set2)#1st method
# print(set1.union(set2))#2nd method
# print(set1&set2)
# print(set1.intersection(set2))
# #set difference
# print(set1-set2)
# print(set1.difference(set2))
# #symetric difference
# print(set1^set2)
# print(set1.symmetric_difference(set2))
#two sum
def twosum(nums,target):
    n = len(nums)
    dict1={}
    for i in range(n):
        rem= target-nums[i]
        if rem in dict1:
            return[dict1[rem],i]

        dict1[nums[i]]=i
nums=[1,2,3,4,5,7]
target=12
print(twosum(nums,target))
#if arr is sorted
# def twosum(nums,target):
#     left=0
#     right=len(nums)-1
#     while(left<right):
#         sum1=nums[left]+nums[right]
#         if sum1==target:
#             return(left+1,right+1)
#         elif sum1>target:
#             right-=1
#         else:
#             left+=1
#     return sum1
# nums=[1,2,3,4,5,11,20,34]
# target=23
# print(twosum(nums,target))
#intersection of two array
# def intersection1(nums1,nums2):
#     return list(set(nums1)&set(nums2))
# nums1=[1,2,3,4]
# nums2=[3,4,5,6]
# print(intersection1(nums1,nums2))
#unique element
# def unique(s):
#     freq={}
#     for i in s:
#         if i not in freq:
#             freq[i]=1
#         else:
#            freq[i]+=1
#     # return freq
#     for i in range(len(s)):
#            if freq[s[i]]==1:
#                   return i
#     return -1

# s='loveleetcode'
# #unique(s)
# print(unique(s))
def anagram(s,t):
    freq={}
    for i in s:
        if i not in freq:
            freq[i]=1
        else:
           freq[i]+=1
    for i in t :
    
    
        if i not in freq:
            return False
        else:
           freq[i]-=1
    return freq

s="love"
t="vole"
print(anagram(s,t))
