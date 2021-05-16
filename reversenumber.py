#reverse the given number 123=321
N=int(input("enter number"))
rev=0
while(N>0):
    remainder=N%10
    rev=(rev*10)+remainder
    N=N//10
print("reverse of number is "+str(rev))