n=int(input("Enter a number:"))
if(n%3==0 and n%5 == 0):
    print("the number is fizzbuzz")
elif(n%3==0):
    print("the number isb fizz")
elif(n%5==0):
    print("the number is buzz")
else:
    print(n)
