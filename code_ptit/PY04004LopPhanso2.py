from math import*

class Pso:
    def __init__(self, tu,mau):
        self.tu= tu
        self.mau = mau
        self.rutgon()
    def rutgon(self):
        k = gcd(self.tu,self.mau)
        self.tu //=k
        self.mau //=k
        return self.tu, self.mau
    
    def add (self, other):
        
        tuw = (self.tu *other.mau)+(other.tu *self.mau)
        maux = self.mau * other.mau
        return Pso(tuw, maux)
    
    def out(self):
        print(f'{self.rutgon()[0]}/{self.rutgon()[1]}')
    
if __name__ == '__main__':
    tu1, mau1,tu2,mau2 = map(int,input().split())
    p = Pso(tu1,mau1)
    q = Pso(tu2,mau2)
    p.add(q).out()

