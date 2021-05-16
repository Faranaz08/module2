#Find the sum of square of first n natural numbers
N= int(input("enter number"))

i= N
sum=0
while(i>=1):
    sum = sum+i**2
    i=i-1
print("sum of square "+str(N) +" natural numbers is " + str(sum))