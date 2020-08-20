"""
几何模块
"""
from __future__ import annotations
import math


class Vec:
    """二维向量"""

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __add__(self, o: Vec) -> Vec:
        """向量相加"""
        return Vec(self.x + o.x, self.y + o.y)

    def __sub__(self, other: Vec) -> Vec:
        """向量相减"""
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Vec:
        """向量乘以标量"""
        return Vec(self.x * other, self.y * other)

    def __truediv__(self, other):
        """向量除法标量"""
        return Vec(self.x / other, self.y / other)

    def dot(self, o: Vec) -> float:
        """点积

        表示当前向量在o向量上的投影长度 乘以 o向量的长度
        """
        return self.x * o.x + self.y * o.y

    def fork(self, o: Vec) -> float:
        """叉乘"""
        return self.x * o.y + self.y * o.x

    def __repr__(self):
        return f'(x={self.x},y={self.y})'

    def __eq__(self, other: Vec):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.__repr__())

    def len2(self) -> float:
        """向量的模的平方"""
        return self.x ** 2 + self.y ** 2

    def len(self) -> float:
        """向量模"""
        return math.sqrt(self.len2())

    def vertical(self, o: Vec) -> bool:
        """判断向量是否垂直"""
        return self.dot(o) == 0

    def parallel(self, o: Vec) -> bool:
        """判断向量是否平行"""
        return self.x * o.y == self.y * o.x


class Line:
    """直线"""

    def __init__(self, st: Vec, ed: Vec):
        self.st = st
        self.ed = ed

    def point_on_line(self, p: Vec) -> bool:
        """点是否在直线上"""
        v1 = self.st - self.ed
        v2 = p - self.ed
        return v1.parallel(v2)

    def point_line_dist2(self, p: Vec) -> float:
        """点到直线距离的平方"""
        v1 = self.st - self.ed
        v2 = p - self.ed
        v4 = v2 - v1 * (v2.dot(v1) / v1.len2())
        return v4.len2()

    def point_line_dist(self, p: Vec) -> float:
        """点到直线的距离"""
        return math.sqrt(self.point_line_dist2(p))


class Segment(Line):
    """线段"""

    def __init__(self, st: Vec, ed: Vec):
        super(Segment, self).__init__(st, ed)
