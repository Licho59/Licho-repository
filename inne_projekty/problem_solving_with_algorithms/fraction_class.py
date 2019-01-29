def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)
        
    def getNum(self):
        return self.num
        
    def getDen(self):
        return self.den

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
             self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
         
    def __mul__(self, other):
        num_num = self.num * other.num
        den_num = self.den * other.den
        common = gcd(num_num, den_num)
        return Fraction(num_num//common, den_num//common)
        
    def __truediv__(self, other):
        num_div = self.num * other.den
        den_div = self.den * other.num
        common = gcd(num_div, den_div)
        return Fraction(num_div//common, den_div//common)
        
    def __sub__(self, other):
        num_sub = self.num * other.den - self.den * other.num
        den_sub = self.den * other.den
        common = gcd(num_sub, den_sub)
        return Fraction(num_sub//common, den_sub//common)
    
    def __lt__(self, other):
        num_lt = self.num * other.den - self.den * other.num
        return num_lt < 0
        
    def __gt__(self, other):
        num_gt = self.num * other.den - self.den * other.num
        return num_gt > 0
        
x = Fraction(1, 2)
y = Fraction(2, 3)
z = Fraction(4, 9)
print(x + y)
print(x == y)
print(x*z)
print(y/z)
print(x-z)
print(x<z)
print(y>z)