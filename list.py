# def maxprofit(prices):
#     min_price=prices[0]
#     profit=0
#     sell_price=0
#     for i in range(1,len(prices)):
#         curr_price=prices[i]-min_price
#         if curr_price>profit:
#             profit=curr_price
#         if prices[i]<min_price:
#             min_price=prices[i]
#         min_price=min(min_price,prices[i])
#     return [min_price,profit,sell_price]
   
# prices=[7,1,5,3,6,4,2,3,4]
# print(maxprofit(prices))
# def dailyprofit(prices):
#     profit=0
#     n=len(prices)
#     for i in range(n-1):
#         if prices[i]>prices[i+1]:
#             profit+=prices[i]-prices[i+1]
#     return profit
# prices=[7,1,5,3,6,4,2,3,4,5,6,8]
# print(dailyprofit(prices))
#matrix
# def maxwealth(accounts):
#     ans=0
#     for account in accounts:
#         ans=max(ans,sum(account))
#     return ans
# accounts=[[5,1,8,7,3],[2,9,6,5,1],[3,2,1,1,8],[8,1,9,2,3]]
# print(maxwealth(accounts))
# spiral matrix
# def spiralorder(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     total = m * n

#     ans = []
#     c = 0

#     colstart = 0
#     rowstart = 0
#     colend = n - 1
#     rowend = m - 1

#     while c < total:

#         # rowstart, colstart -> colend
#         for i in range(colstart, colend + 1):
#             ans.append(matrix[rowstart][i])
#             c += 1

#         if c == total:
#             break

#         rowstart += 1

#         # colend, rowstart -> rowend
#         for i in range(rowstart, rowend + 1):
#             ans.append(matrix[i][colend])
#             c += 1

#         if c == total:
#             break

#         colend -= 1

#         # rowend, colend -> colstart
#         for i in range(colend, colstart - 1, -1):
#             ans.append(matrix[rowend][i])
#             c += 1

#         if c == total:
#             break

#         rowend -= 1

#         # colstart, rowend -> rowstart
#         for i in range(rowend, rowstart - 1, -1):
#             ans.append(matrix[i][colstart])
#             c += 1

#         if c == total:
#             break

#         colstart += 1

#     return ans


# matrix = [
#     [1, 2, 5, 6, 1],
#     [8, 2, 9, 3, 4],
#     [2, 8, 1, 2, 6],
#     [9, 2, 3, 5, 1]
# ]

# print(spiralorder(matrix))
def spiralorder(matrix): 
    m = len(matrix) 
    n = len(matrix[0]) 
    total = m * n 
 
    ans = [] 
    c = 0 
 
    colstart = 0 
    rowstart = 0 
    colend = n - 1 
    rowend = m - 1 

    while c < total: 

        # ❌ ERROR: matrix[i][rowstart]
        # Row ko fix karke column change karna hai
        # Correct: matrix[rowstart][i]
        for i in range(colstart, colend + 1): 
            ans.append(matrix[rowstart][i])
            c += 1

        rowstart += 1

        if c == total: 
            break 

        # Right column: top -> bottom
        for i in range(rowstart, rowend + 1): 
            ans.append(matrix[i][colend])
            c += 1

        colend -= 1

        if c == total: 
            break 

        # ❌ ERROR: range(colend, colstart + 1)
        # +1 ki wajah se last element skip ho jayega
        # Correct: range(colend, colstart - 1, -1)
        #
        # ❌ ERROR: matrix[i][rowend]
        # Row fix hai, column i change hona chahiye
        # Correct: matrix[rowend][i]
        for i in range(colend, colstart - 1, -1): 
            ans.append(matrix[rowend][i])
            c += 1

        rowend -= 1

        if c == total: 
            break 

        # ❌ ERROR: range(rowend, rowstart + 1)
        # Reverse direction mein -1 chahiye
        # Correct: range(rowend, rowstart - 1, -1)
        #
        # ❌ ERROR: matrix[i][colstart] actually YAHAN correct hai
        # because column fixed hai aur row i change ho raha hai
        for i in range(rowend, rowstart - 1, -1): 
            ans.append(matrix[i][colstart])
            c += 1

        colstart += 1

    return ans 


matrix = [ 
    [1, 2, 5, 6, 1], 
    [8, 2, 9, 3, 4], 
    [2, 8, 1, 2, 6], 
    [9, 2, 3, 5, 1]
] 
 
print(spiralorder(matrix))