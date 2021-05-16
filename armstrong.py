#check given nor is armstrong or not 153=1**3+5**3+3**3
N=int(input(("enter the number")))
i=N
sum=0
n=0
while(N>0):
    n=N%10
    cube=n**3

    sum=sum+cube
    N = N // 10
print(sum)
if(sum==i):
    print("given number is amstrong")
else:
    print("given number is not a amstrong")