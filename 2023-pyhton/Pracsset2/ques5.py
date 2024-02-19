def startsandendwithvowel(str):
    str=str.lower()
    if str[0] in "aeiou" and str[-1] in "aeiou":
        return True
    else:
        return False
    
def main():
    str=input("Enter a string: ")
    words=str.split(" ")
    for word in words:
        if startsandendwithvowel(word):
            print(word)
            
            
    
    
if __name__ == "__main__":
    main()