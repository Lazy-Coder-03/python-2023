import math

def myPow(x,n):
    if n==0:
        return 1
    else:
        return x*myPow(x,n-1)

def myFact(x):
    if x==0:
        return 1
    else:
        return x*myFact(x-1)
    
def myCos(x,n):
    x=math.radians(x)
    cosx=0
    for i in range(n):
        cosx+=(myPow(-1,i))*(myPow(x,2*i))/myFact(2*i)
    return round(cosx,7)
    
def main():
    x=int(input("Enter the angle in degrees: "))
    n=int(input("Enter the number of terms: "))
    print("The result is:",myCos(x,n))
        
        
if __name__ == "__main__":
    main()