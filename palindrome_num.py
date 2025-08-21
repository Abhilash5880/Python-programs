number=str(input("Enter a number"))
num2=number
palin=True
k=0
for i in range(len(number)-1,-1,-1):
    #print(i," ",k,"\n")
    if(number[k]==number[i]):
        palin=True
    if(number[k]!=number[i]):
        palin=False
        break
    k=k+1
    #print("Iteration : ",k,"\n")
    #print(palin)
print("Palindrome : ",palin)
