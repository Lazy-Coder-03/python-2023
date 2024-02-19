import math

class cNum:
    def __init__(self,r=0,i=0):
        self.real=r
        self.img=i
        
    def addC(self,other):
        return cNum(self.real+other.real,self.img+other.img)
    
    def __add__(self,other):
        return self.addC(other)
        
    def mulC(self,other):
        return cNum((self.real*other.real)+(self.img*other.img),(self.img*other.real)+(self.real*other.img))
    
    def __mul__(self,other):
        return self.mulC(other)
    
    def __str__(self):
        if self.img<0:
            return f"{self.real}{self.img}i"
        else: 
            return f"{self.real}+{self.img}i"    
    
    def findMod(self):
        return math.sqrt((self.real**2)+(self.img**2))
    
    def findTheta(self):
        if self.real==0:
            return math.inf
        else:
            return math.degrees(math.atan(self.img/self.real))
        
def main():
    c1=cNum(4,3)
    c2=cNum(5,0)
    c3=cNum(3,-1)
    print(c1+c2)
    print(c2*c3)
    print("Modulus of c3:",c3.findMod())
    print("Theta of c3:",c3.findTheta())


if __name__=="__main__":
    main()    