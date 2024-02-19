def monotonically_asc(arr):
    startInd=0
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            startInd=i+1
    if len(arr[startInd:])<=1:
        return None    
    else:       
        return arr[startInd:]
    
    
def monotonically_desc(arr):
    startInd=0
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            startInd=i+1
    if len(arr[startInd:])<=1:
        return None    
    else:       
        return arr[startInd:]            


def main():
    n=int(input("Enter the number of total elements: "))
    arr=[]
    for _ in range(n):
        arr.append(int(input("Enter the element: ")))
    print("The list is: ",arr)
    c=int(input("Do u want the list spliced in ascending order(1) or descending order(2): "))
    if c==1:
        x=monotonically_asc(arr)
        if x==None:
            print("Nil")
        else:
            print("The monotonically increasing list is: ",x)
    elif c==2:
        x=monotonically_desc(arr)
        if x==None:
            print("Nil")
        else:
            print("The monotonically decreasing list is: ",x)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()