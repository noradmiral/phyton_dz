class Complex:
    def __init__(self, real, mnim):
        self.z = complex(real, mnim)

    def __str__(self):
        return str(f'{self.z.real} + {self.z.imag} j')

    def __mul__(self, other):
        r = self.z.real * other.z.real - self.z.imag * other.z.imag
        m = self.z.imag * other.z.real + self.z.real * other.z.imag
        return Complex(r,m)

    def __add__(self, other):
        return Complex((self.z.real + other.z.real), (self.z.imag + other.z.imag))


a = Complex(22,2)
b = Complex(3,41)
print(a + b)
print(a * b)


# class ComplexNumber:
#     def __init__(self, a, b, *args):
#         self.a = a
#         self.b = b
#         self.z = 'a + b * i'
#
#     def __add__(self, other):
#         print(f'Сумма z1 и z2 равна')
#         return f'z = {self.a + other.a} + {self.b + other.b} * i'
#
#     def __mul__(self, other):
#         print(f'Произведение z1 и z2 равно')
#         return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'
#
#     def __str__(self):
#         return f'z = {self.a} + {self.b} * i'
#
#
# z_1 = ComplexNumber(1, -2)
# z_2 = ComplexNumber(3, 4)
# print(z_1)
# print(z_1 + z_2)
# print(z_1 * z_2)
