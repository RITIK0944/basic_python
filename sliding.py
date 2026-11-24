#number without reapiting character
# s = 'cadbzabcd'
# left = 0
# ans = 0
# seen = {}
# for right in range(len(s)):
#     if s[right] in seen and seen[s[right]] >= left:
#         left = seen[s[right]] + 1
#     seen[s[right]] = right
#     ans = max(ans, right - left + 1)
# print(ans)
#max consecutive ones
# arr=[1,1,1,0,0,0,1,1,1,1,0]
# k=2
# # k=2
# # left=0
# # ans=0
# # count=0
# # for i in range(len(arr)):
# #     if arr[i]==0:
# #         count+=1
# #     while count>k:
# #         if arr[left]==0:
# #             count-=1
# #         left+=1
# #     ans=max(ans,i-left+1)
# # print(ans)
# def max_consecutive_ones(arr,k):
#     left=0
#     ans=0
#     count=0
#     for i in range(len(arr)):
#         if arr[i]==0:
#             count+=1
#         if count>k:
#             if arr[left]==0:
#                 count-=1
#             left+=1
#         ans=max(ans,i-left+1)
#     return ans
# print(max_consecutive_ones(arr,k))    
#fruit basket
# arr=[3,3,3,1,2,1,1,2,3,3,4]
# s='my name is ritik'
# s = list(s)
# n=len(s)
# for i in range(0,n):
#     for j in range(n-1,0,-1):
#         if s[i]==' ' or s[j]==' ':
#             temp=s[i]
#             s[i]=s[j]
#             s[j]=temp
# print(''.join(s))
# s = 'my name is ritik'
# words = s.split()
# words.reverse()
# print(' '.join(words))
#fruit basket
# arr=[3,3,3,1,2,1,1,2,3,3,4]
# k=2
# def max_len(arr,k):
#     max_length=0
#     n=len(arr)
#     for i in range(n):
#         my_set=set()
#         for j in range(i,n):
#             my_set.add(arr[j])
#             if len(my_set)>k:
#                 break
#             max_length=max(max_length,j-i+1)
#     return max_length
# print(max_len(arr,k))
# def max_len_opt(arr,k):
#     left=0
#     right=0
#     max_length=0
#     my_dict={}
#     n=len(arr)
#     while(right<n):
#         my_dict[arr[right]]=my_dict.get(arr[right],0)+1
#         if len(my_dict)>k:
#             my_dict[arr[left]]-=1
#             if(my_dict[arr[left]]==0):
#                 del my_dict[arr[left]]
#             left+=1
#         max_length=max(max_length,right-left+1)
#         right+=1
#     return max_length
# print(max_len_opt(arr,k))  
s='aaabbccd'
k=2
def max_len1(s,k):
    n=len(s)
    max_length=0
    for i in range(n):
        my_set=set()
        for j in range(i,n):
            my_set.add(s[j])
            if len(my_set)>k:
                break
            max_length=max(max_length,j-i+1)
    return max_length
print(max_len1(s,k))  
