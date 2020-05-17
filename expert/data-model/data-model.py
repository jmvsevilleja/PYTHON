class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{})'.format(self.coeffs)


p1 = Polynomial(1, 2, 3, 4)  # x^2 + 2X + 3
p2 = Polynomial(3, 4, 3)  # 3x^2 + 4x + 3
