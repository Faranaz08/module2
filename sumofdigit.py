#find the sum of digits give  number 12=1+2=3
N=int(input("enter number"))
dig=0
sum=0
while(N>0):
    dig=N%10
    sum=sum+int(dig)
    N=N/10
print("the sum of digits of is "+str(sum))