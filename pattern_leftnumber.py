n =int(input("Enter series range : \n"))

k=n-2
for i in range (n): #if n is 5, will run upto 4 
    
    num=1
    j=0
    while(j<=k):
        print("_",end=" ")
        j+=1
    for m in range (j,n,1):
        print(num,end=" ")
        num+=1
    k-=1

    print("\n")