"""
自定义一个类，并实现一些魔法函数。
"""
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # 获取对象的字符串表示，如未定义会返回<Vector object at 0x10e100070>形式
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        # 返回向量模长
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        # 布尔运算符，必须返回一个布尔值，和if一起使用时可以用来判断一个对象是否为空
        # 如果没有实现__bool__，python会自动调用__len__
        return bool(abs(self))
    
    def __add__(self, other):
        # 自定义加法，相当于重载加法运算符
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        # 重载乘法运算符
        return Vector(self.x * scalar, self.y * scalar)
    
v1 = Vector(2, 4)
v2 = Vector(3, 1)
print(v1 + v2)
print(abs(v1))
print(v1 * 3)
print(abs(v1*3))

