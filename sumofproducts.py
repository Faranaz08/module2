#find the product of the digits of given number 12=1*2=2
N=int(input("enter number"))
product=1
dig=0
while(N!=0):
    dig=N%10
    N = N // 10
    product= product * int(dig)

print("the product of digits of is "+str(product))
if(product==0):
    print("enter a number without zero")
