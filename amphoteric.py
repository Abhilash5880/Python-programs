r1=int(input("Enter lower range "))
r2=int(input("Enter upper range "))

for i in range(r1,r2+1):
    l2=i**2
    l=len(str(i))

    if(l2%(10**(l))==i):
        print(i," -> ",l2)
