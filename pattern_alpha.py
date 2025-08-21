
ch=str(input("Enter the alphabet till which u want to the series : "))
c=""   
c=ch.upper()
k=ord(c)+1
for i in range(65,ord(c)+1):

    for i in range(65,ord(c)+1,1):
        if(i>=k):
            print(" ",end=" ")
            continue
        print(chr(i), end=" ")
    for i in range(ord(c)-1,64,-1):
        if(i>=k):
            print(" ",end=" ")
            continue
        print(chr(i), end=" ")
    print("\n")
    k-=1
