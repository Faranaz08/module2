#given  number  prime or not
N=int(input("enter a number"))
i=2
while(N>i):
    if N%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break

