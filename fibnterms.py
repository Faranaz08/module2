#print the fibonacci series 0,1,1,2,3,5,8,13....n
nterm = int(input("How many fibonacci terms? "))
n1 = 0
n2 = 1
i=0
while i<nterm:
    print(n1)
    next_t=n1+n2
    n1=n2
    n2=next_t
    i=i+1
