def recPow(base,power):
    if power == 0:
        return 1
    else:
        return base*recPow(base,power-1)
    
def main():
    base=int(input("Enter the base: "))
    power=int(input("Enter the power: "))
    print("The result is: ",recPow(base,power))
    
    
if __name__ == "__main__":
    main()