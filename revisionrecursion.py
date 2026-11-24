# n= int(input("enter your number: "))
# def f(i,n):
#     if i>n:
#         return 
#     print('Ritik')
#     
#     return(f(i+1,n)) 

# f(1,n)
# n= int(input("enter your number: "))
# def f(i,n):
#     if i<=0:
#         return 
#     print(i)
#     return(f(i-1,n)) 

# f(n,n)
#print 1 to n  linearaly
# n= int(input("enter your number: "))
# def f(i,n):
#     if i<1:
#         return 
#     f(i-1,n)
#     print(i)
# f(n,n)
# sum of 1 to n 
# n= int(input("enter your number: "))
# def f(i,sum):
#     if i<1:
        
#         return sum
#     return f(i-1,sum+i)
# ans=f(n,0)
# print(ans)
# def f(n):
#     if n==0:
#         return 0
#     return f(n-1)+n
# ans=f(n)
# print(ans)
#reverse an array
#arr=[1,2,3,4,5]
# def f(l,r):
#     if l>=r:
#         return
#     arr[l],arr[r]=arr[r],arr[l]
#     return f(l+1,r-1)
# f(0,len(arr)-1)
# print(arr)
# arr = [1, 2, 3, 4, 5]

# n = len(arr)

# def f(i):

#     if i >= n // 2:
#         return

#     arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

#     f(i+1)

# f(0)

# print(arr)
# s= input('enter a string: ')
# def f(i):
#     if i>= len(s)//2:
#         return True
#     if s[i]!=s[len(s)-i-1]:
#         return False
#     return f(i+1)
# ans=f(0)
# print(ans) 
#multiple recursion call
#fibonacci series 
# def f(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return f(n-1)+f(n-2)
    

# print(f(52))