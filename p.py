num=int(input("enter num:"))
i=1
c=0
while i<=num:
    if num%i==0:
        c=c+1
    i=i+1
if c==2:
    print(num,"prime")
else:
    print(num,"not prime")