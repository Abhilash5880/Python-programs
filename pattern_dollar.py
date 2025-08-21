for i in range (0,5,1):
    for j in range(0,5,1):
        if(i==j or i+j==4):
            print("$", end=" ")
            continue
        if((i!=4 and i!=0) and (j!=4 and j!=0) and (i+j==3 or i+j==5)):
            print(" ", end=" ")
            continue
        else:
            print("*", end=" ")
            continue
    print("\n")
            