#find the sum of even numbers from 1 to n
N= int(input("enter number"))
sum=0
i=1

while(i<=N):
    if(i%2==0):
        sum = sum+i
    i=i+1


print("sum of  "+str(N) +" even numbers is " + str(sum))
