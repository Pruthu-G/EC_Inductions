class ComplexNumber:
    """A class to perform operations on complex numbers."""

    def __init__(self, real, imag):
        """Initialize the complex number."""
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """Add two complex numbers."""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """Subtract two complex numbers."""
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """Multiply two complex numbers."""
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        """Divide two complex numbers."""
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    def __str__(self):
        """String representation of the complex number."""
        return f"{self.real} + {self.imag}i"
