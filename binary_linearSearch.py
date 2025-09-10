arr=[]
n=int(input("Enter number of elements in list\n"))
print("Enter the elements\n")
for i in range(n):
    arr.append(int(input()))

print("Original array\n",arr)

def sorting(L,n):
    temp=0;
    for i in range(0,n-1,1):
        for j in range(0,n-i-1,1):
            if(L[j]>L[j+1]):
                L[j],L[j+1]=L[j+1],L[j]
    return L
'''
def linear(L,n):
    print("---Linear search---")
    target=int(input("Enter the target element to search\n"))
    for i in range(n):
        if L[i]==target:
            print("Element found at index ",i," \n")
            return

    print("Element not found\n")
'''
def binary(L, n):
    sorted_list = sorting(L, n)

    print("---Binary search---")
    low = 0
    high = n - 1

    target = int(input("Enter the target element to search\n"))
    
    while low <= high:
        mid = (low + high) // 2
        
        if sorted_list[mid] == target:
            print("Element found at index ", mid, "\n")
            return  # Exits the function once the element is found
        elif target < sorted_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    # This line is only reached if the loop finishes without finding the element
    print("Element not found\n")
#linear(arr,n)
binary(arr,n)
 