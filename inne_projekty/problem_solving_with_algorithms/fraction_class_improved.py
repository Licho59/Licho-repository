def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        try: bottom > 0 # it allows negative denominators
        except: pass
        
        assert isinstance(top, int) # it will check if not integer
        assert isinstance(bottom, int)
        self.num = top // common
        self.den = bottom // common
        

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, other):
        if isinstance(other, int):
            num_num = self.num + other * self.den
            den_num = self.den
            return Fraction(num_num, den_num)
        else:
            num_num = self.num * other.den + self.den * other.num
            den_num = self.den * other.den
        return Fraction(num_num, den_num)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __mul__(self, other):
        num_num = self.num * other.num
        den_num = self.den * other.den
        return Fraction(num_num, den_num)

    def __truediv__(self, other):
        num_div = self.num * other.den
        den_div = self.den * other.num
        return Fraction(num_div, den_div)

    def __sub__(self, other):
        num_sub = self.num * other.den - self.den * other.num
        den_sub = self.den * other.den
        return Fraction(num_sub, den_sub)

    def __lt__(self, other):
        num_lt = self.num * other.den - self.den * other.num
        return num_lt < 0
        
    def __le__(self, other):
        num_le = self.num * other.den - self.den * other.num
        return num_le <= 0

    def __gt__(self, other):
        num_gt = self.num * other.den - self.den * other.num
        return num_gt > 0
        
    def __ge__(self, other):
        num_ge = self.num * other.den - self.den * other.num
        return num_ge >= 0


x = Fraction(1, 2)
y = Fraction(1, -4)
z = Fraction(-4, 9)
u = Fraction(2, -8)
w = 2
print(x + y)
print(x == y)
print(x * z)
print(y / z)
print(x - z)
print(x < z)
print(y > z)
print(u>=y)
print(u!=y)
print(x+w)
print(w+x)
