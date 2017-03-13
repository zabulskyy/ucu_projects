from unittest import TestCase
from line_intersect import *


class TestLineIntersect(TestCase):
    def test_line_intersect(self):
        self.assertEquals((0.5, 0.5), line_intersect([(0.0, 0.0),(1.0, 1.0)], [(1.0, 0.0),(0.0, 1.0)]), "fail")
        self.assertEquals((1.0, 2.0), line_intersect([(1.0, 2.0),(0.0, 0.0)], [(2.0, 4.0),(3.0, 6.0)]), "fail")
        self.assertEquals(None, line_intersect([(0.0, 0.0),(1.0, 1.0)], [(0.0, 1.0),(1.0, 2.0)]), "fail")
        self.assertEquals('invalid function(s)', line_intersect([(1.0, 0.0),(1.0, 1.0)], [(0.0, 1.0),(1.0, 2.0)]), "fail")
