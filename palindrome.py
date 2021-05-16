#check the given number palindrome or not
N=int(input("enter number"))
rev=0
while(N>0):
    remainder=N%10
    rev=(rev*10)+remainder
    N=N//10
if(N==rev):
    print("Given number is palindrome"+str(rev))
else:
    print("Given number is not a palindrome")