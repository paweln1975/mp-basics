"""
Class represents complex number z = a + b*i
a = real part
b = imaginery number

>>> cn_pos = ComplexNumber(10, 10)
>>> assert type(cn_pos) is ComplexNumber
>>> cn_pos
10 + 10i

>>> cn_neg = ComplexNumber(10, -2)
>>> assert type(cn_neg) is ComplexNumber
>>> cn_neg
10 - 2i
"""


class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        """
        Addition of complex numbers.
        >>> cn1 = ComplexNumber(1, 2)
        >>> cn2 = ComplexNumber(3, 4)
        >>> cn1 + cn2
        4 + 6i
        """
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        return ComplexNumber(real, imaginary)


    def __sub__(self, other):
        """
        Addition of complex numbers.
        >>> cn1 = ComplexNumber(1, 2)
        >>> cn2 = ComplexNumber(3, 4)
        >>> cn1 - cn2
        -2 - 2i
        """
        real = self.real_part - other.real_part
        imaginary = self.im_part - other.im_part
        return ComplexNumber(real, imaginary)


    def __mul__(self, other):
        """
        Multiplication of complex numbers.
        >>> cn1 = ComplexNumber(1, 2)
        >>> cn2 = ComplexNumber(3, 4)
        >>> cn1 * cn2
        -5 + 10i
        """
        real = (self.real_part * other.real_part -
                self.im_part * other.im_part)
        imaginary = (self.real_part * other.im_part +
                     other.real_part * self.im_part)
        return ComplexNumber(real, imaginary)

    def __iadd__(self, other):
        """
        Addition with assignment (+=) for complex numbers.
        >>> z1 = ComplexNumber(8, -3)
        >>> z2 = ComplexNumber(-6, 2)
        >>> z1 += z2
        >>> z1
        2 - 1i
        """
        self.real_part += other.real_part
        self.im_part += other.im_part
        return self

    def __eq__(self, other):
        """
        Compare two complex numbers for equality (==).
        >>> z1 = ComplexNumber(5, -5)
        >>> z2 = ComplexNumber(5, -5)
        >>> z3 = ComplexNumber(4, 4)
        >>> z1 == z2
        True
        >>> z1 == z3
        False

        """
        return ((self.real_part == other.real_part) and
                (self.im_part == other.im_part))

    def __repr__(self):
        sign = '+' if self.im_part > 0 else '-'
        return f'{self.real_part} {sign} {abs(self.im_part)}i'
