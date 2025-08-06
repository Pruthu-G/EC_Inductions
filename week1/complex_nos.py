import math

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        return Complex(
            self.real * no.real - self.imaginary * no.imaginary,
            self.real * no.imaginary + self.imaginary * no.real
        )

    def __truediv__(self, no):
        denominator = no.real**2 + no.imaginary**2
        if denominator == 0:
            raise ZeroDivisionError("division by zero")
        return Complex(
            (self.real * no.real + self.imaginary * no.imaginary) / denominator,
            (self.imaginary * no.real - self.real * no.imaginary) / denominator
        )

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        real = self.real
        imag = self.imaginary
        if imag == 0:
            return "%.2f+0.00i" % real
        elif real == 0:
            sign = '+' if imag >= 0 else '-'
            return "0.00%s%.2fi" % (sign, abs(imag))
        else:
            sign = '+' if imag >= 0 else '-'
            return "%.2f%s%.2fi" % (real, sign, abs(imag))
    
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')