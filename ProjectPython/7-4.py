from math import gcd


class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("分母不能为0")
        common = gcd(int(numerator), int(denominator))
        self.__num = int(numerator) // common
        self.__den = int(denominator) // common
        if self.__den < 0:
            self.__num = -self.__num
            self.__den = -self.__den

    def __str__(self):
        if self.__den == 1:
            return str(self.__num)
        return f"{self.__num}/{self.__den}"

    def __repr__(self):
        return f"Fraction({self.__num}, {self.__den})"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        n = self.__num * other.__den + other.__num * self.__den
        d = self.__den * other.__den
        return Fraction(n, d)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        n = self.__num * other.__den - other.__num * self.__den
        d = self.__den * other.__den
        return Fraction(n, d)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return other.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self.__num * other.__num, self.__den * other.__den)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if other.__num == 0:
            raise ZeroDivisionError("除数不能为0")
        return Fraction(self.__num * other.__den, self.__den * other.__num)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return other.__truediv__(self)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.__num / self.__den == other
        return self.__num == other.__num and self.__den == other.__den

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.__num * other.__den > other.__num * self.__den
        return self.__num / self.__den > other

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.__num * other.__den < other.__num * self.__den
        return self.__num / self.__den < other

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __getitem__(self, index):
        if index == 0:
            return self.__num
        elif index == 1:
            return self.__den
        raise IndexError("索引0获取分子,索引1获取分母")

    def __call__(self):
        return self.__num / self.__den

    def __abs__(self):
        return Fraction(abs(self.__num), self.__den)


def test():
    print("=== 基础部分 ===")
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 2)
    f3 = Fraction(2, 4)
    print(f"f1: {f1}")
    print(f"f2: {f2}")
    print(f"f3(2/4自动约分): {f3}")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 == f2: {f1 == f2}")
    print(f"f2 == f3: {f2 == f3}")

    print("\n=== 扩展部分 ===")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    print(f"f1 > f2: {f1 > f2}")
    print(f"f1 < f2: {f1 < f2}")
    print(f"f1 >= f2: {f1 >= f2}")
    print(f"f1 + 2 = {f1 + 2}")
    print(f"3 + f2 = {3 + f2}")
    print(f"f1 * 4 = {f1 * 4}")
    print(f"6 / f2 = {6 / f2}")
    print(f"f1[0](分子): {f1[0]}")
    print(f"f1[1](分母): {f1[1]}")
    print(f"f1()小数值: {f1():.3f}")
    print(f"abs(Fraction(-3,4)): {abs(Fraction(-3, 4))}")


if __name__ == "__main__":
    test()
